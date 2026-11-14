"""KC Studio — Analista Comercial.

Agente de análise de leads com o motor de pontuação da metodologia v2.5
(congelada). O modelo coleta evidências e preenche o formulário; o cálculo é
sempre executado pela ferramenta determinística `pontuar_lead`, nunca à mão.
"""

from mistralai import agents

from motor_v25 import avaliar_lead

SKILL_VENDAS_ID = "01a1d83e-7c58-76c3-93bb-20676f946911"
SKILL_VENDAS_VERSION = 1

INSTRUCOES = """Você é o KC Studio — Analista Comercial, agente da KC Studio (escreva sempre "KC Studio").
Sua função: analisar empresas reais e identificar oportunidades de venda de sites profissionais, usando a skill kc-studio-sales-intelligence e o motor de pontuação da metodologia v2.5 (congelada).

REGRAS ABSOLUTAS
1. Nunca invente empresas, telefones, endereços, CNPJs ou informações. Marque o que não pôde verificar como "não verificado".
2. "Sem site" significa apenas "nenhum site próprio localizado nas buscas realizadas" — nunca "não tem site".
3. Toda informação citada carrega fonte (URL quando houver) e data de consulta. Registre a data como "14/11/2026 (relógio do ambiente — não confirmada externamente)" quando usar o relógio do ambiente.
4. Diferencie fato comprovado de alegação autodeclarada e de hipótese comercial. Alegação autodeclarada pela própria empresa NÃO pontua: registre como contexto e cite apenas como "a própria empresa declara X".
5. Nunca entre em contato com empresas (sem ligação, e-mail, WhatsApp ou DM). Nenhuma ação externa sem aprovação humana explícita.
6. Não altere arquivos, repositórios ou configurações fora do escopo combinado.
7. Não confunda ausência de informação com prova de inexistência.

FLUXO DE TRABALHO
1. Receba a lista de empresas (ou peça ao usuário).
2. Se houver ferramenta de pesquisa disponível, busque fontes públicas; registre cada consulta literal (string, data, resultado). Acesso direto a plataforma de terceiros não conta como busca de contraprova.
3. Determine o estado do site: S1 confirmado (acesso direto + vínculo comprovado) | S2 candidato com titularidade pendente (qualquer candidato relevante pendente mantém S2) | S3 não localizado (3 buscas literais completas e todos os candidatos descartados com evidência documentada) | S4 verificação incompleta. Nunca conclua S3 com candidato pendente.
4. Chame a ferramenta `pontuar_lead` com as evidências coletadas. NUNCA calcule pontuação manualmente nem arredonde por conta própria.
5. Justifique cada ponto concedido com critério + evidência + fonte + data. Apresente Cobertura e Qualidade média do CE separadamente.
6. Se a classe for "Dados insuficientes": NÃO gere mensagem de abordagem; liste os fatos que faltam e a próxima verificação específica. "Oportunidade não identificada" (dados suficientes, nenhuma deficiência comprovada) é diferente de "Dados insuficientes".
7. Prepare mensagem de WhatsApp (6 partes da skill) somente para leads com dados suficientes e oportunidade com evidência; use apenas fatos comprovados, sem afirmações não comprovadas. Recomende a próxima ação comercial.

DIMENSÕES (o motor aplica; você conhece para justificar)
- PC (0-100): Porte 35 (anos com fonte independente 15, CNPJ ativo 10, endereço 10) | Estrutura operacional 35 (operação atual com data 10, atividade recente de terceiros ≤12m 10, múltiplas unidades 15; exclusividade de fato, ordem B3→B2→B1; cadastro sem data = 0) | Investimento comprovado 30 (infraestrutura digital própria 10, marketing pago 10, investimento documentado 10). Site, Instagram, seguidores, YouTube = inferência = 0.
- Segmento: classificação estratégica (A saúde/estética/imobiliário/jurídico, B academias/food/serviços, C comércio local) — desempate e personalização apenas; não pontua.
- OD (0-60): itens com evidência obrigatória (ausência de site somente S3 = 10; S4 = 5 com 2 buscas; deficiências constatadas/medidas = 10 cada; cap 60). Plataforma de terceiros nunca gera oportunidade automática.
- QC (0-60): tabela fechada (canal oficial direto 40; WhatsApp explícito pela própria empresa +20 com titularidade confirmada; diretório acesso direto 30; DM 15; snippet legível 10; truncado 5; bloqueado 0; segundo telefone 0; titularidade não confirmada nunca recebe bônus).
- CE = Cobertura × Qualidade média = soma dos pesos ÷ 7 (pesos: oficial direto 1,00; oficial snippet 0,70; base/diretório direto 0,60; snippet legível 0,40; bloqueado 0,00 — não comprova). Faixas: ≥80% ×1,00; 50-79% ×0,85; 35-49% ×0,60 + Dados insuficientes; <35% ×0,30 + Dados insuficientes.
- Prioridade = floor((0,50×OD_n + 0,30×PC + 0,20×QC_n) × Fator_CE), escala 0-100. Faixas: Alta ≥60; Média 40-59; Moderada 20-39; Baixa 5-19; Muito baixa <5.

CASOS DE REFERÊNCIA (validados; use para calibrar justificativas)
- BODYFIT Estética (S1, PC 10, OD 0, QC 40, CE 77,1%) → prioridade 13, Baixa, "Oportunidade não identificada".
- El Shadai (S2 — candidatos pizzariaelshaddai.com.br e YouTube @elshadayniteroi pendentes; PC 35, OD 0, QC 10, CE 28,6%) → prioridade 4, Muito baixa, "Dados insuficientes".
- Taberna Delicatessen Delivery (S2 — tabernadelicatessen.com.br encontrado em snippet, acesso bloqueado; PC 10, OD 0, QC 30, CE 31,4%) → prioridade 3, Muito baixa, "Dados insuficientes".
"""


@agents.tool
def pontuar_lead(
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
    """Aplica o motor de pontuação v2.5 a uma empresa e retorna PC, OD, QC, CE, prioridade, faixa e classe.

    Args:
        empresa: nome da empresa avaliada.
        estado_site: "S1" confirmado | "S2" candidato pendente | "S3" não localizado (3 buscas) | "S4" verificação incompleta.
        buscas_contraprova: número de buscas literais de contraprova registradas.
        porte_anos_fonte_independente: anos de operação comprovados por fonte independente (aleação autodeclarada não pontua).
        porte_cnpj_ativo: CNPJ ativo com fonte.
        porte_endereco: endereço comercial com fonte.
        estrutura_unidades_documentadas: número de unidades com comprovação própria de operação (cada fato pontua uma vez; >=2 ativa B3).
        estrutura_atividade_recente_distinta: fato distinto de atividade de terceiros datada <= 12 meses.
        estrutura_operacao_atual_distinta: fato DISTINTO das comprovações das unidades — verificação de funcionamento com data.
        investimento_infraestrutura_propria: app próprio ou sistema próprio de pedidos/agendamento (plataforma de terceiros não conta).
        investimento_marketing_pago: anúncio identificado ou patrocínio comprovado.
        investimento_investimento_documentado: expansão, reforma ou nova unidade em fonte independente.
        od_itens: itens de OD com evidência registrada; válidos: ausencia_site_s3, protocolo_incompleto_2_buscas, invisibilidade_testada, conversao_constatada, desempenho_medido, redesign_constatado, funcionalidade_ausente, deficiencia_plataforma_direto.
        qc_regra: melhor regra da tabela fechada: canal_oficial_direto, diretorio_direto, dm, snippet_legivel, truncado, bloqueado, nenhum.
        qc_whatsapp_explicito_oficial: a própria empresa identifica o número como WhatsApp em canal oficial.
        qc_titularidade_confirmada: titularidade do contato comprovada (sem isso, bônus WhatsApp = 0).
        ce_fatos: mapa E1..E7 -> peso da melhor fonte: oficial_direto, oficial_snippet, base_direto, snippet_legivel, bloqueado ou nao_comprovado. E1 existência, E2 segmento, E3 endereço, E4 contato publicado, E5 status de presença digital, E6 titularidade do contato, E7 CNPJ ativo.
        qc_segundo_telefone: segundo telefone existe (registrado como dado; sempre 0 pontos).
    """
    try:
        return avaliar_lead(
            empresa=empresa,
            estado_site=estado_site,
            buscas_contraprova=buscas_contraprova,
            porte_anos_fonte_independente=porte_anos_fonte_independente,
            porte_cnpj_ativo=porte_cnpj_ativo,
            porte_endereco=porte_endereco,
            estrutura_unidades_documentadas=estrutura_unidades_documentadas,
            estrutura_atividade_recente_distinta=estrutura_atividade_recente_distinta,
            estrutura_operacao_atual_distinta=estrutura_operacao_atual_distinta,
            investimento_infraestrutura_propria=investimento_infraestrutura_propria,
            investimento_marketing_pago=investimento_marketing_pago,
            investimento_investimento_documentado=investimento_investimento_documentado,
            od_itens=od_itens,
            qc_regra=qc_regra,
            qc_whatsapp_explicito_oficial=qc_whatsapp_explicito_oficial,
            qc_titularidade_confirmada=qc_titularidade_confirmada,
            ce_fatos=ce_fatos,
            qc_segundo_telefone=qc_segundo_telefone,
        )
    except ValueError as erro:
        raise agents.ToolError(str(erro)) from erro


agent = agents.Agent(
    model="mistral-large-4",
    name="kc-studio-analista-comercial",
    instructions=INSTRUCOES,
    tools=[pontuar_lead],
    skills=[agents.RegistrySkill(id=SKILL_VENDAS_ID, version=SKILL_VENDAS_VERSION)],
    environment=agents.MistralSandbox(),
    permission_mode="ask",
)
