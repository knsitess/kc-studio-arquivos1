"""Motor determinístico de pontuação da metodologia KC Studio v2.5.

Sem chamadas externas, IA, rede ou credenciais. Entradas precisam ser evidências
registradas pelo operador; campos ausentes nunca são presumidos como verdadeiros.
"""
from __future__ import annotations

from math import floor
from typing import Any

CE_WEIGHTS = {
    "official_direct": 1.0,
    "official_snippet": 0.7,
    "registry_direct": 0.6,
    "readable_snippet": 0.4,
    "blocked": 0.0,
}
CE_FACTS = ("E1", "E2", "E3", "E4", "E5", "E6", "E7")
CRITICAL_FACTS = ("E1", "E2", "E4", "E5")


def _valid_evidence(item: dict[str, Any]) -> bool:
    return bool(item.get("source_url") and item.get("verified_on"))


def _unique_scored(items: list[dict[str, Any]]) -> tuple[int, list[str]]:
    """Pontua cada fato/evidência uma vez; exige URL e data."""
    seen: set[str] = set()
    total = 0
    accepted: list[str] = []
    for item in items:
        fact_id = str(item.get("fact_id", "")).strip()
        if not fact_id or fact_id in seen or not _valid_evidence(item):
            continue
        seen.add(fact_id)
        points = int(item.get("points", 0))
        if points < 0:
            raise ValueError("Pontos de evidência não podem ser negativos.")
        total += points
        accepted.append(fact_id)
    return total, accepted


def calculate_pc(data: dict[str, Any]) -> dict[str, Any]:
    """PC 0–100. Cada critério exige evidence com fact_id, source_url e verified_on."""
    a_items = data.get("porte", [])
    a, a_ids = _unique_scored(a_items)

    # Estrutura: B3 tem precedência sobre B2, que tem precedência sobre B1.
    structure = data.get("estrutura", {})
    b_items: list[dict[str, Any]] = []
    units = structure.get("multiple_units", [])
    valid_units = [u for u in units if _valid_evidence(u)]
    if valid_units:
        for unit in valid_units:
            b_items.append({**unit, "fact_id": f"B3:{unit.get('unit_id', '')}", "points": 15})
    else:
        for key, points in (("recent_third_party_activity", 10), ("current_operation", 10)):
            item = structure.get(key)
            if item and _valid_evidence(item):
                b_items.append({**item, "fact_id": key, "points": points})
                break
    b, b_ids = _unique_scored(b_items)

    c_items = data.get("investimento", [])
    c, c_ids = _unique_scored(c_items)
    raw = a + b + c
    return {"score": min(100, raw), "raw_score": raw, "porte_a": a,
            "estrutura_b": b, "investimento_c": c,
            "scored_evidence": a_ids + b_ids + c_ids}


def calculate_od(data: dict[str, Any]) -> dict[str, Any]:
    status = data.get("site_status", "S4")
    if status not in {"S1", "S2", "S3", "S4"}:
        raise ValueError("site_status deve ser S1, S2, S3 ou S4.")
    points = 10 if status == "S3" else 0
    reasons = ["ausencia_de_site_confirmada"] if status == "S3" else []
    if status == "S4":
        searches = int(data.get("completed_searches", 0))
        if searches >= 2:
            points += 5
            reasons.append("verificacao_incompleta_duas_buscas")
    for key in ("invisibility_tested", "conversion_issue_confirmed",
                "performance_measured_issue", "redesign_confirmed",
                "missing_functionality_confirmed", "platform_page_deficiency_confirmed"):
        item = data.get(key)
        if item and _valid_evidence(item):
            points += 10
            reasons.append(key)
    return {"score": min(60, points), "reasons": reasons}


def calculate_qc(data: dict[str, Any]) -> dict[str, Any]:
    kind = data.get("channel_type", "none")
    points_by_kind = {
        "official_direct": 40, "directory_direct": 30, "dm": 15,
        "readable_snippet": 10, "truncated_snippet": 5, "blocked": 0, "none": 0,
    }
    if kind not in points_by_kind:
        raise ValueError("channel_type inválido.")
    evidence = data.get("evidence", {})
    points = points_by_kind[kind] if _valid_evidence(evidence) else 0
    if points and kind == "official_direct" and data.get("whatsapp_identified_by_company"):
        whatsapp = data.get("whatsapp_evidence", {})
        if _valid_evidence(whatsapp):
            points += 20
    return {"score": min(60, points), "channel_type": kind}


def calculate_ce(data: dict[str, Any]) -> dict[str, Any]:
    facts = data.get("facts", {})
    weights = []
    missing_critical = []
    missing = []
    for fact in CE_FACTS:
        item = facts.get(fact)
        if not item or not _valid_evidence(item):
            weight = 0.0
            missing.append(fact)
        else:
            level = item.get("evidence_level", "blocked")
            if level not in CE_WEIGHTS:
                raise ValueError(f"evidence_level inválido em {fact}: {level}")
            weight = CE_WEIGHTS[level]
        weights.append(weight)
        if fact in CRITICAL_FACTS and weight == 0:
            missing_critical.append(fact)
    coverage = sum(1 for w in weights if w > 0) / 7
    quality = sum(weights) / 7
    ce = quality * 100
    if ce >= 80:
        factor = 1.0
    elif ce >= 50:
        factor = 0.85
    elif ce >= 35:
        factor = 0.60
    else:
        factor = 0.30
    site_status = data.get("site_status", "S4")
    di_reasons = []
    if missing_critical:
        di_reasons.append("fatos_criticos_sem_comprovacao:" + ",".join(missing_critical))
    if ce < 50:
        di_reasons.append("CE_abaixo_de_50")
    if data.get("protocol_complete") is not True:
        di_reasons.append("protocolo_incompleto")
    if site_status == "S2":
        di_reasons.append("site_candidato_sem_resolucao")
    return {"ce_percent": round(ce, 1), "coverage_percent": round(coverage * 100, 1),
            "quality_percent": round(quality * 100, 1), "factor": factor,
            "data_insufficient": bool(di_reasons), "di_reasons": di_reasons,
            "missing_facts": missing}


def calculate_priority(pc: int, od: int, qc: int, ce_factor: float) -> dict[str, Any]:
    if not 0 <= pc <= 100 or not 0 <= od <= 60 or not 0 <= qc <= 60:
        raise ValueError("PC deve ser 0–100; OD e QC devem ser 0–60.")
    if ce_factor not in {0.30, 0.60, 0.85, 1.0}:
        raise ValueError("Fator CE inválido.")
    od_n, qc_n = od / 60 * 100, qc / 60 * 100
    score = min(100, floor((0.50 * od_n + 0.30 * pc + 0.20 * qc_n) * ce_factor))
    if score >= 60:
        band = "Alta"
    elif score >= 40:
        band = "Média"
    elif score >= 20:
        band = "Moderada"
    elif score >= 5:
        band = "Baixa"
    else:
        band = "Muito baixa"
    return {"score": score, "band": band}


def evaluate_lead(data: dict[str, Any]) -> dict[str, Any]:
    pc = calculate_pc(data.get("pc", {}))
    od = calculate_od(data.get("od", {}))
    qc = calculate_qc(data.get("qc", {}))
    ce = calculate_ce(data.get("ce", {}))
    priority = calculate_priority(pc["score"], od["score"], qc["score"], ce["factor"])
    blocked = ce["data_insufficient"]
    return {"pc": pc, "od": od, "qc": qc, "ce": ce, "priority": priority,
            "funnel_status": "Pendente de verificação" if blocked else "Aguardando revisão humana",
            "approach_allowed": False}
