"""Motor de pontuação KC Studio — Metodologia v2.5 (congelada).

Implementa fielmente as regras aprovadas na revisão v2.5:

- PC (0-100): Porte 35 | Estrutura operacional 35 (com exclusividade de fato,
  ordem B3 -> B2 -> B1) | Investimento comprovado 30.
    * Alegações autodeclaradas NÃO pontuam: o motor só aceita fatos com fonte.
    * Site, Instagram, seguidores e YouTube = inferência = 0 pontos.
    * Cadastro em diretório/plataforma sem indicador de atualização = 0 pontos
      em unidade ativa (cadastro != operação comprovada).
- OD (0-60): itens com evidência obrigatória; ausência de site pontua SOMENTE
  no estado S3 (3 buscas literais e todos os candidatos descartados);
  plataforma de terceiros nunca gera oportunidade automática.
- QC (0-60): tabela fechada de contato; WhatsApp +20 somente se explicitamente
  identificado pela própria empresa em canal oficial E titularidade confirmada;
  segundo telefone = 0.
- CE = Cobertura x Qualidade média = soma dos pesos / 7, sobre os 7 fatos
  essenciais; fato só em fonte bloqueada (peso 0,00) não é comprovado.
- Prioridade = floor((0,50xOD_n + 0,30xPC + 0,20xQC_n) x Fator_CE), escala 0-100
  com OD_n = OD/60x100 e QC_n = QC/60x100.
- Dados insuficientes (gatilhos): fato crítico (E1/E2/E4/E5) não comprovado,
  CE < 50%, protocolo de contraprova incompleto, site em S2.
"""

from __future__ import annotations

import math

PESOS_FONTE = {
    "oficial_direto": 1.00,
    "oficial_snippet": 0.70,
    "base_direto": 0.60,
    "snippet_legivel": 0.40,
    "bloqueado": 0.00,
}
NAO_COMPROVADO = "nao_comprovado"

ESTADOS_SITE = ("S1", "S2", "S3", "S4")
FATOS_ESSENCIAIS = ("E1", "E2", "E3", "E4", "E5", "E6", "E7")
FATOS_CRITICOS = ("E1", "E2", "E4", "E5")

PC_COMPONENTES = {
    "A": {"anos_fonte_independente": 15, "cnpj_ativo": 10, "endereco": 10},
    "B": {"b1_operacao_atual": 10, "b2_atividade_recente": 10, "b3_multiplas_unidades": 15},
    "C": {"infraestrutura_digital_propria": 10, "marketing_pago": 10, "investimento_documentado": 10},
}

OD_ITENS = {
    "ausencia_site_s3": 10,
    "protocolo_incompleto_2_buscas": 5,
    "invisibilidade_testada": 10,
    "conversao_constatada": 10,
    "desempenho_medido": 10,
    "redesign_constatado": 10,
    "funcionalidade_ausente": 10,
    "deficiencia_plataforma_direto": 10,
}
OD_CAP = 60

QC_REGRAS = {
    "canal_oficial_direto": 40,
    "diretorio_direto": 30,
    "dm": 15,
    "snippet_legivel": 10,
    "truncado": 5,
    "bloqueado": 0,
    "nenhum": 0,
}
QC_BONUS_WHATSAPP = 20
QC_MAX = 60

FAIXAS_PRIORIDADE = ((60, "Alta"), (40, "Média"), (20, "Moderada"), (5, "Baixa"), (0, "Muito baixa"))


def fator_ce(ce: float) -> tuple[float, str]:
    if ce >= 0.80:
        return 1.00, "Alta"
    if ce >= 0.50:
        return 0.85, "Média"
    if ce >= 0.35:
        return 0.60, "Baixa"
    return 0.30, "Crítica"


def faixa_prioridade(prioridade: int) -> str:
    for limite, nome in FAIXAS_PRIORIDADE:
        if prioridade >= limite:
            return nome
    return "Muito baixa"


def pontuar_bloco_b(
    unidades_documentadas: int,
    atividade_recente_distinta: bool,
    operacao_atual_distinta: bool,
) -> dict[str, int]:
    """Regra de exclusividade de fato (v2.5): um fato pontua uma vez; ordem B3 -> B2 -> B1.

    - >= 2 unidades com comprovação própria: B3 = 15; os fatos das unidades ficam
      consumidos. Fatos DISTINTOS declarados (atividade recente de terceiros
      datada; verificação de operação atual com data) ainda pontuam B2 e B1.
    - == 1 unidade: o fato da unidade pontua em B1; atividade recente não é
      aceita em separado (presunção conservadora de que é o mesmo fato).
    - == 0 unidades: atividade recente distinta -> B2; senão operação atual -> B1.

    Os flags `atividade_recente_distinta` e `operacao_atual_distinta` devem ser
    usados somente para fatos que NÃO são as comprovações das unidades.
    """
    if unidades_documentadas >= 2:
        return {
            "b1_operacao_atual": 10 if operacao_atual_distinta else 0,
            "b2_atividade_recente": 10 if atividade_recente_distinta else 0,
            "b3_multiplas_unidades": 15,
        }
    if unidades_documentadas == 1:
        return {
            "b1_operacao_atual": 10,
            "b2_atividade_recente": 0,
            "b3_multiplas_unidades": 0,
        }
    if atividade_recente_distinta:
        return {
            "b1_operacao_atual": 0,
            "b2_atividade_recente": 10,
            "b3_multiplas_unidades": 0,
        }
    return {
        "b1_operacao_atual": 10 if operacao_atual_distinta else 0,
        "b2_atividade_recente": 0,
        "b3_multiplas_unidades": 0,
    }


def pontuar_od(estado_site: str, buscas_contraprova: int, itens: list[str]) -> int:
    desconhecidos = [i for i in itens if i not in OD_ITENS]
    if desconhecidos:
        raise ValueError(f"Itens de OD desconhecidos: {desconhecidos}")
    if "ausencia_site_s3" in itens:
        if estado_site != "S3":
            raise ValueError("ausencia_site_s3 exige estado S3")
        if buscas_contraprova < 3:
            raise ValueError("S3 exige 3 buscas literais registradas")
    if "protocolo_incompleto_2_buscas" in itens:
        if estado_site != "S4" or buscas_contraprova != 2:
            raise ValueError("protocolo_incompleto_2_buscas exige estado S4 com 2 buscas")
    if estado_site == "S2" and ("ausencia_site_s3" in itens or "protocolo_incompleto_2_buscas" in itens):
        raise ValueError("S2 (candidato pendente) não permite concluir ausência de site")
    return min(OD_CAP, sum(OD_ITENS[i] for i in itens))


def pontuar_qc(
    regra: str,
    whatsapp_explicito_oficial: bool,
    titularidade_confirmada: bool,
    segundo_telefone: bool = False,
) -> dict:
    if regra not in QC_REGRAS:
        raise ValueError(f"Regra de QC fora da tabela fechada: {regra}")
    base = QC_REGRAS[regra]
    bonus = QC_BONUS_WHATSAPP if (whatsapp_explicito_oficial and titularidade_confirmada) else 0
    total = min(QC_MAX, base + bonus)
    return {
        "base": base,
        "bonus_whatsapp": bonus,
        "segundo_telefone": 0,
        "segundo_telefone_registrado": bool(segundo_telefone),
        "qc": total,
    }


def calcular_ce(fatos: dict[str, str]) -> dict:
    desconhecidos = [k for k in fatos if k not in FATOS_ESSENCIAIS]
    if desconhecidos:
        raise ValueError(f"Fatos essenciais desconhecidos: {desconhecidos}")
    comprovados: dict[str, float] = {}
    for eid in FATOS_ESSENCIAIS:
        valor = fatos.get(eid, NAO_COMPROVADO)
        if valor == NAO_COMPROVADO:
            continue
        if valor not in PESOS_FONTE:
            raise ValueError(f"Peso de fonte inválido para {eid}: {valor}")
        peso = PESOS_FONTE[valor]
        if peso <= 0:
            continue
        comprovados[eid] = peso
    cobertura = len(comprovados) / len(FATOS_ESSENCIAIS)
    qualidade = (sum(comprovados.values()) / len(comprovados)) if comprovados else 0.0
    ce = cobertura * qualidade
    soma = sum(comprovados.values())
    conferencia = soma / len(FATOS_ESSENCIAIS)
    if abs(ce - conferencia) > 1e-9:
        raise ValueError("Identidade CE = soma dos pesos / 7 violada")
    fator, faixa = fator_ce(ce)
    return {
        "comprovados": sorted(comprovados),
        "cobertura": cobertura,
        "qualidade_media": qualidade,
        "ce": ce,
        "conferencia_soma_sobre_7": conferencia,
        "faixa": faixa,
        "fator": fator,
    }


def avaliar_dados_insuficientes(estado_site: str, buscas: int, ce_info: dict, fatos: dict[str, str]) -> tuple[bool, list[str]]:
    motivos: list[str] = []
    for eid in FATOS_CRITICOS:
        valor = fatos.get(eid, NAO_COMPROVADO)
        if valor == NAO_COMPROVADO or PESOS_FONTE.get(valor, 0.0) <= 0:
            motivos.append(f"fato crítico {eid} não comprovado")
    if ce_info["ce"] < 0.50:
        motivos.append("CE < 50%")
    if estado_site == "S2":
        motivos.append("site em estado S2 (candidato com titularidade pendente)")
    if estado_site == "S4" or (estado_site == "S3" and buscas < 3):
        motivos.append("protocolo de contraprova incompleto")
    return bool(motivos), motivos


def calcular_prioridade(pc: int, od: int, qc: int, fator: float) -> int:
    od_n = od / OD_CAP * 100
    qc_n = qc / QC_MAX * 100
    return math.floor((0.50 * od_n + 0.30 * pc + 0.20 * qc_n) * fator)


def avaliar_lead(
    empresa: str,
    estado_site: str,
    buscas_contraprova: int,
    porte_anos_fonte_independente: bool,
    porte_cnpj_ativo: bool,
    porte_endereco: bool,
    estrutura_unidades_documentadas: int,
    estrutura_atividade_recente_distinta: bool,
    estrutura_operacao_atual_distinta: bool,
    investimento_infraestrutura_propria: bool,
    investimento_marketing_pago: bool,
    investimento_investimento_documentado: bool,
    od_itens: list[str],
    qc_regra: str,
    qc_whatsapp_explicito_oficial: bool,
    qc_titularidade_confirmada: bool,
    ce_fatos: dict[str, str],
    qc_segundo_telefone: bool = False,
) -> dict:
    if estado_site not in ESTADOS_SITE:
        raise ValueError(f"Estado de site inválido: {estado_site}")

    bloco_a = sum(
        [
            15 if porte_anos_fonte_independente else 0,
            10 if porte_cnpj_ativo else 0,
            10 if porte_endereco else 0,
        ]
    )
    bloco_b_map = pontuar_bloco_b(estrutura_unidades_documentadas, estrutura_atividade_recente_distinta, estrutura_operacao_atual_distinta)
    bloco_b = sum(bloco_b_map.values())
    bloco_c = sum(
        [
            10 if investimento_infraestrutura_propria else 0,
            10 if investimento_marketing_pago else 0,
            10 if investimento_investimento_documentado else 0,
        ]
    )
    pc = bloco_a + bloco_b + bloco_c
    if pc > 100:
        raise ValueError("PC acima de 100")

    od = pontuar_od(estado_site, buscas_contraprova, list(od_itens))
    qc_info = pontuar_qc(qc_regra, qc_whatsapp_explicito_oficial, qc_titularidade_confirmada, qc_segundo_telefone)
    ce_info = calcular_ce(ce_fatos)
    insuficiente, motivos = avaliar_dados_insuficientes(estado_site, buscas_contraprova, ce_info, ce_fatos)
    prioridade = calcular_prioridade(pc, od, qc_info["qc"], ce_info["fator"])

    if insuficiente:
        classe = "Dados insuficientes"
    elif od == 0:
        classe = "Oportunidade não identificada"
    else:
        classe = "Oportunidade com evidência registrada"

    return {
        "empresa": empresa,
        "estado_site": estado_site,
        "pc": {"total": pc, "bloco_a_porte": bloco_a, "bloco_b_estrutura": bloco_b_map, "bloco_c_investimento": bloco_c},
        "od": od,
        "qc": qc_info,
        "ce": ce_info,
        "dados_insuficientes": insuficiente,
        "motivos_dados_insuficientes": motivos,
        "prioridade": prioridade,
        "faixa": faixa_prioridade(prioridade),
        "classe": classe,
    }
