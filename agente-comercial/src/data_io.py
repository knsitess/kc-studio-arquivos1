"""Entrada e saída JSON do Analista Comercial KC Studio.

Não pesquisa nem cria empresas. Recebe dados e evidências fornecidos pelo operador,
executa o motor determinístico e produz um relatório JSON rastreável.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scoring import evaluate_lead


def validate_payload(payload: Any) -> None:
    if not isinstance(payload, dict):
        raise ValueError("A raiz do arquivo JSON deve ser um objeto.")
    business = payload.get("business")
    if not isinstance(business, dict):
        raise ValueError("Campo obrigatório ausente ou inválido: business.")
    for field in ("name", "city", "segment"):
        value = business.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"business.{field} é obrigatório e não pode ficar vazio.")
    if not isinstance(payload.get("pc", {}), dict):
        raise ValueError("pc deve ser um objeto JSON.")
    if not isinstance(payload.get("od", {}), dict):
        raise ValueError("od deve ser um objeto JSON.")
    if not isinstance(payload.get("qc", {}), dict):
        raise ValueError("qc deve ser um objeto JSON.")
    if not isinstance(payload.get("ce", {}), dict):
        raise ValueError("ce deve ser um objeto JSON.")


def _walk_evidence(value: Any):\n    """Percorre objetos/listas sem presumir que campos sejam evidência."""\n    if isinstance(value, dict):\n        if "source_url" in value or "verified_on" in value:\n            yield value\n        for child in value.values():\n            yield from _walk_evidence(child)\n    elif isinstance(value, list):\n        for child in value:\n            yield from _walk_evidence(child)\n\n\ndef build_report(payload: dict[str, Any]) -> dict[str, Any]:
    validate_payload(payload)
    evaluation = evaluate_lead({key: payload.get(key, {}) for key in ("pc", "od", "qc", "ce")})
    return {
        "schema_version": "1.0",
        "business": payload["business"],
        "evaluation": evaluation,
        "operational_control": {
            "source_records_supplied": any(\n                isinstance(item, dict) and bool(item.get("source_url"))\n                for section in ("pc", "od", "qc", "ce")\n                for item in _walk_evidence(payload.get(section, {}))\n            ),
            "human_review_required": True,
            "approach_allowed": False,
            "warning": "A pontuação não valida a veracidade das fontes. Revise cada evidência antes de qualquer decisão.",
        },
    }


def load_payload(path: str | Path) -> dict[str, Any]:
    try:
        with Path(path).open("r", encoding="utf-8") as file:
            payload = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON inválido na linha {exc.lineno}, coluna {exc.colno}: {exc.msg}") from exc
    validate_payload(payload)
    return payload


def save_report(report: dict[str, Any], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Avalia um registro empresarial usando a metodologia KC Studio v2.5.")
    parser.add_argument("input", help="Caminho do arquivo JSON de entrada.")
    parser.add_argument("-o", "--output", help="Caminho opcional para salvar o relatório JSON.")
    args = parser.parse_args()
    try:
        payload = load_payload(args.input)
        report = build_report(payload)
        rendered = json.dumps(report, ensure_ascii=False, indent=2)
        if args.output:
            save_report(report, args.output)
            print(f"Relatório salvo em: {args.output}")
        else:
            print(rendered)
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f"Erro: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
