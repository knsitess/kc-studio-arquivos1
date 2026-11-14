"""Testes locais gratuitos do motor v2.5 — não chamam a API da Mistral.

Casos de referência validados na revisão v2.5 (BODYFIT 13, El Shadai 4,
Taberna 3) e regras estruturais (teto, piso, exclusividade de fato, tabelas
fechadas, estados de site, gatilhos de dados insuficientes).
"""

import math

import pytest

from motor_v25 import (
    FATOS_CRITICOS,
    OD_ITENS,
    PESOS_FONTE,
    avaliar_dados_insuficientes,
    avaliar_lead,
    calcular_ce,
    calcular_prioridade,
    faixa_prioridade,
    fator_ce,
    pontuar_bloco_b,
    pontuar_od,
    pontuar_qc,
)


def base(**substituicoes):
    parametros = dict(
        empresa="Teste",
        estado_site="S1",
        buscas_contraprova=0,
        porte_anos_fonte_independente=False,
        porte_cnpj_ativo=False,
        porte_endereco=False,
        estrutura_unidades_documentadas=0,
        estrutura_atividade_recente_distinta=False,
        estrutura_operacao_atual_distinta=False,
        investimento_infraestrutura_propria=False,
        investimento_marketing_pago=False,
        investimento_investimento_documentado=False,
        od_itens=[],
        qc_regra="nenhum",
        qc_whatsapp_explicito_oficial=False,
        qc_titularidade_confirmada=False,
        ce_fatos={},
        qc_segundo_telefone=False,
    )
    parametros.update(substituicoes)
    return parametros


CE_BODYFIT = {
    "E1": "oficial_direto",
    "E2": "oficial_direto",
    "E3": "snippet_legivel",
    "E4": "oficial_direto",
    "E5": "oficial_direto",
    "E6": "oficial_direto",
    "E7": "nao_comprovado",
}

CE_EL_SHADAI = {
    "E1": "snippet_legivel",
    "E2": "snippet_legivel",
    "E3": "snippet_legivel",
    "E4": "snippet_legivel",
    "E5": "nao_comprovado",
    "E6": "nao_comprovado",
    "E7": "snippet_legivel",
}

CE_TABERNA = {
    "E1": "base_direto",
    "E2": "base_direto",
    "E3": "snippet_legivel",
    "E4": "base_direto",
    "E5": "nao_comprovado",
    "E6": "nao_comprovado",
    "E7": "nao_comprovado",
}


class TestCasosDeReferencia:
    def test_bodyfit(self):
        resultado = avaliar_lead(**base(empresa="BODYFIT Estética", estado_site="S1", porte_endereco=True, qc_regra="canal_oficial_direto", qc_titularidade_confirmada=True, ce_fatos=CE_BODYFIT))
        assert resultado["pc"]["total"] == 10
        assert resultado["od"] == 0
        assert resultado["qc"]["qc"] == 40
        assert resultado["ce"]["ce"] == pytest.approx(5.4 / 7)
        assert resultado["ce"]["faixa"] == "Média"
        assert resultado["ce"]["fator"] == 0.85
        assert resultado["dados_insuficientes"] is False
        assert resultado["prioridade"] == 13
        assert resultado["faixa"] == "Baixa"
        assert resultado["classe"] == "Oportunidade não identificada"

    def test_el_shadai(self):
        resultado = avaliar_lead(**base(empresa="El Shadai", estado_site="S2", buscas_contraprova=3, porte_anos_fonte_independente=True, porte_cnpj_ativo=True, porte_endereco=True, qc_regra="snippet_legivel", ce_fatos=CE_EL_SHADAI))
        assert resultado["pc"]["total"] == 35
        assert resultado["od"] == 0
        assert resultado["qc"]["qc"] == 10
        assert resultado["ce"]["ce"] == pytest.approx(2.0 / 7)
        assert resultado["ce"]["faixa"] == "Crítica"
        assert resultado["dados_insuficientes"] is True
        assert resultado["prioridade"] == 4
        assert resultado["faixa"] == "Muito baixa"
        assert resultado["classe"] == "Dados insuficientes"

    def test_taberna(self):
        resultado = avaliar_lead(**base(empresa="Taberna Delicatessen Delivery", estado_site="S2", buscas_contraprova=1, porte_endereco=True, qc_regra="diretorio_direto", ce_fatos=CE_TABERNA))
        assert resultado["pc"]["total"] == 10
        assert resultado["od"] == 0
        assert resultado["qc"]["qc"] == 30
        assert resultado["ce"]["ce"] == pytest.approx(2.2 / 7)
        assert resultado["dados_insuficientes"] is True
        assert resultado["prioridade"] == 3
        assert resultado["faixa"] == "Muito baixa"
        assert resultado["classe"] == "Dados insuficientes"

    def test_identidade_ce_soma_sobre_7(self):
        for ce_fatos in (CE_BODYFIT, CE_EL_SHADAI, CE_TABERNA):
            info = calcular_ce(ce_fatos)
            assert info["ce"] == pytest.approx(info["conferencia_soma_sobre_7"])
            assert info["ce"] == pytest.approx(info["cobertura"] * info["qualidade_media"])


class TestLimitesGlobais:
    def test_teto_global_100(self):
        ce_todos = {f"E{i}": "oficial_direto" for i in range(1, 8)}
        todos_od = [i for i in OD_ITENS if i != "protocolo_incompleto_2_buscas"]
        resultado = avaliar_lead(**base(estado_site="S3", buscas_contraprova=3, porte_anos_fonte_independente=True, porte_cnpj_ativo=True, porte_endereco=True, estrutura_unidades_documentadas=2, estrutura_atividade_recente_distinta=True, estrutura_operacao_atual_distinta=True, investimento_infraestrutura_propria=True, investimento_marketing_pago=True, investimento_investimento_documentado=True, od_itens=todos_od, qc_regra="canal_oficial_direto", qc_whatsapp_explicito_oficial=True, qc_titularidade_confirmada=True, ce_fatos=ce_todos))
        assert resultado["pc"]["total"] == 100
        assert resultado["od"] == 60
        assert resultado["qc"]["qc"] == 60
        assert resultado["ce"]["ce"] == 1.0
        assert resultado["prioridade"] == 100
        assert resultado["faixa"] == "Alta"

    def test_piso_zero(self):
        resultado = avaliar_lead(**base(estado_site="S3", buscas_contraprova=3))
        assert resultado["pc"]["total"] == 0
        assert resultado["od"] == 0
        assert resultado["qc"]["qc"] == 0
        assert resultado["ce"]["ce"] == 0.0
        assert resultado["prioridade"] == 0
        assert resultado["faixa"] == "Muito baixa"
        assert resultado["dados_insuficientes"] is True

    def test_normalizacao_pesos_efetivos(self):
        od_n = 60 / 60 * 100
        qc_n = 60 / 60 * 100
        assert math.floor((0.50 * od_n + 0.30 * 100 + 0.20 * qc_n) * 1.00) == 100


class TestBlocoBExclusividade:
    def test_duas_unidades_sem_fatos_distintos(self):
        blocos = pontuar_bloco_b(unidades_documentadas=2, atividade_recente_distinta=False, operacao_atual_distinta=False)
        assert blocos == {"b1_operacao_atual": 0, "b2_atividade_recente": 0, "b3_multiplas_unidades": 15}

    def test_bloco_b_teto_35_com_fatos_distintos(self):
        blocos = pontuar_bloco_b(unidades_documentadas=2, atividade_recente_distinta=True, operacao_atual_distinta=True)
        assert blocos == {"b1_operacao_atual": 10, "b2_atividade_recente": 10, "b3_multiplas_unidades": 15}

    def test_duas_unidades_com_atividade_distinta(self):
        blocos = pontuar_bloco_b(unidades_documentadas=2, atividade_recente_distinta=True, operacao_atual_distinta=False)
        assert blocos["b3_multiplas_unidades"] == 15
        assert blocos["b2_atividade_recente"] == 10
        assert blocos["b1_operacao_atual"] == 0

    def test_una_unidade_vai_para_b1(self):
        blocos = pontuar_bloco_b(unidades_documentadas=1, atividade_recente_distinta=True, operacao_atual_distinta=False)
        assert blocos == {"b1_operacao_atual": 10, "b2_atividade_recente": 0, "b3_multiplas_unidades": 0}

    def test_sem_unidade_atividade_recente_prevalece(self):
        blocos = pontuar_bloco_b(unidades_documentadas=0, atividade_recente_distinta=True, operacao_atual_distinta=True)
        assert blocos == {"b1_operacao_atual": 0, "b2_atividade_recente": 10, "b3_multiplas_unidades": 0}

    def test_sem_unidade_somente_operacao_atual(self):
        blocos = pontuar_bloco_b(unidades_documentadas=0, atividade_recente_distinta=False, operacao_atual_distinta=True)
        assert blocos["b1_operacao_atual"] == 10


class TestQCTabelaFechada:
    def test_bonus_whatsapp_exige_titularidade(self):
        com_titularidade = pontuar_qc("canal_oficial_direto", True, True)
        sem_titularidade = pontuar_qc("canal_oficial_direto", True, False)
        assert com_titularidade["qc"] == 60
        assert sem_titularidade["qc"] == 40
        assert sem_titularidade["bonus_whatsapp"] == 0

    def test_segundo_telefone_nao_pontua(self):
        resultado = pontuar_qc("canal_oficial_direto", True, True, segundo_telefone=True)
        assert resultado["qc"] == 60
        assert resultado["segundo_telefone"] == 0
        assert resultado["segundo_telefone_registrado"] is True

    def test_regra_fora_da_tabela(self):
        with pytest.raises(ValueError):
            pontuar_qc("instagram", False, False)

    def test_bloqueado_nao_comprova(self):
        assert pontuar_qc("bloqueado", False, False)["qc"] == 0


class TestOD:
    def test_cap_60(self):
        itens_s3 = [i for i in OD_ITENS if i != "protocolo_incompleto_2_buscas"]
        assert pontuar_od("S3", 3, itens_s3) == 60

    def test_s2_bloqueia_ausencia(self):
        with pytest.raises(ValueError):
            pontuar_od("S2", 3, ["ausencia_site_s3"])

    def test_s3_exige_tres_buscas(self):
        with pytest.raises(ValueError):
            pontuar_od("S3", 2, ["ausencia_site_s3"])
        assert pontuar_od("S3", 3, ["ausencia_site_s3"]) == 10

    def test_protocolo_incompleto_exige_s4_com_duas_buscas(self):
        with pytest.raises(ValueError):
            pontuar_od("S4", 1, ["protocolo_incompleto_2_buscas"])
        assert pontuar_od("S4", 2, ["protocolo_incompleto_2_buscas"]) == 5

    def test_item_desconhecido(self):
        with pytest.raises(ValueError):
            pontuar_od("S1", 0, ["item_inexistente"])


class TestCE:
    def test_bloqueado_nao_comprova(self):
        info = calcular_ce({f"E{i}": "bloqueado" for i in range(1, 8)})
        assert info["cobertura"] == 0.0
        assert info["ce"] == 0.0

    def test_ce_alta_exige_qualidade_alta(self):
        pesos = list(PESOS_FONTE.values())
        for peso_a in pesos:
            for peso_b in pesos:
                fatos = {f"E{i}": None for i in range(1, 8)}
                valores = {k: "oficial_direto" if v == 1.0 else "oficial_snippet" if v == 0.7 else "base_direto" if v == 0.6 else "snippet_legivel" if v == 0.4 else "bloqueado" for k, v in fatos.items()}
                valores["E1"] = "oficial_direto" if peso_a == 1.0 else {1.0: "oficial_direto", 0.7: "oficial_snippet", 0.6: "base_direto", 0.4: "snippet_legivel", 0.0: "bloqueado"}[peso_a]
                valores["E2"] = "oficial_direto" if peso_b == 1.0 else {1.0: "oficial_direto", 0.7: "oficial_snippet", 0.6: "base_direto", 0.4: "snippet_legivel", 0.0: "bloqueado"}[peso_b]
                info = calcular_ce(valores)
                if info["ce"] >= 0.80:
                    assert info["qualidade_media"] >= 0.80

    def test_peso_invalido(self):
        with pytest.raises(ValueError):
            calcular_ce({"E1": "twitter"})

    def test_fato_desconhecido(self):
        with pytest.raises(ValueError):
            calcular_ce({"E9": "oficial_direto"})


class TestDadosInsuficientes:
    def test_fato_critico_ausente(self):
        ce_info = calcular_ce({k: "oficial_direto" for k in ("E2", "E3", "E6", "E7")})
        insuficiente, motivos = avaliar_dados_insuficientes("S1", 0, ce_info, {"E2": "oficial_direto", "E3": "oficial_direto", "E6": "oficial_direto", "E7": "oficial_direto"})
        assert insuficiente is True
        assert any("E1" in m for m in motivos)

    def test_fato_complementar_ausente_nao_trava(self):
        fatos = {k: "oficial_direto" for k in ("E1", "E2", "E4", "E5")}
        ce_info = calcular_ce(fatos)
        insuficiente, _ = avaliar_dados_insuficientes("S1", 0, ce_info, fatos)
        assert insuficiente is False

    def test_ce_baixo_trava(self):
        fatos = {k: "snippet_legivel" for k in ("E1", "E2", "E4", "E5")}
        ce_info = calcular_ce(fatos)
        insuficiente, motivos = avaliar_dados_insuficientes("S1", 0, ce_info, fatos)
        assert insuficiente is True
        assert any("CE" in m for m in motivos)

    def test_s2_trava(self):
        fatos = {k: "oficial_direto" for k in ("E1", "E2", "E4", "E5")}
        ce_info = calcular_ce(fatos)
        insuficiente, motivos = avaliar_dados_insuficientes("S2", 0, ce_info, fatos)
        assert insuficiente is True
        assert any("S2" in m for m in motivos)


class TestFaixasEFatores:
    def test_fator_ce_faixas(self):
        assert fator_ce(0.80) == (1.00, "Alta")
        assert fator_ce(0.79) == (0.85, "Média")
        assert fator_ce(0.50) == (0.85, "Média")
        assert fator_ce(0.49) == (0.60, "Baixa")
        assert fator_ce(0.35) == (0.60, "Baixa")
        assert fator_ce(0.34) == (0.30, "Crítica")

    def test_faixas_prioridade(self):
        assert faixa_prioridade(100) == "Alta"
        assert faixa_prioridade(60) == "Alta"
        assert faixa_prioridade(59) == "Média"
        assert faixa_prioridade(40) == "Média"
        assert faixa_prioridade(39) == "Moderada"
        assert faixa_prioridade(20) == "Moderada"
        assert faixa_prioridade(19) == "Baixa"
        assert faixa_prioridade(5) == "Baixa"
        assert faixa_prioridade(4) == "Muito baixa"
        assert faixa_prioridade(0) == "Muito baixa"

    def test_floor_unico(self):
        assert calcular_prioridade(10, 0, 40, 0.85) == math.floor((0 + 3 + 13.333333333333334) * 0.85) == 13


class TestValidacoes:
    def test_estado_invalido(self):
        with pytest.raises(ValueError):
            avaliar_lead(**base(estado_site="S5"))

    def test_s2_com_ausencia_levanta_erro(self):
        with pytest.raises(ValueError):
            avaliar_lead(**base(estado_site="S2", buscas_contraprova=3, od_itens=["ausencia_site_s3"]))
