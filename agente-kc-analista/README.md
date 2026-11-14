# KC Studio — Analista Comercial

Agente de análise de leads para venda de sites profissionais, com o motor de
pontuação da **metodologia v2.5 (congelada)** implementado em módulo próprio e
exposto ao modelo como ferramenta determinística.

## Estrutura

```
agente-kc-analista/
├── main.py              # agente (mistralai-agents 1.1) + ferramenta pontuar_lead
├── motor_v25.py         # motor de pontuação v2.5 (puro Python, sem dependências)
├── tests/
│   └── test_motor_v25.py
├── pyproject.toml
├── .env.example
└── README.md
```

## Conexão com a skill

A skill `kc-studio-sales-intelligence` (UUID `01a1d83e-7c58-76c3-93bb-20676f946911`, versão 1)
é anexada via `agents.RegistrySkill(id=..., version=1)`. Skills são servidas como
arquivos no sandbox, por isso o agente usa `environment=agents.MistralSandbox()`
(o `NoSandbox` padrão recusa skills). Criar sandbox Mistral exige a permissão
`cloud_user` do workspace.

## Como executar

```bash
cd agente-kc-analista
uv sync                                  # instala Python 3.12+ e dependências
uv run pytest                            # testes locais gratuitos (não chamam a API)
uv run agents --version                  # verifica a CLI do SDK
uv run agents info                       # valida entrypoint e capacidades
cp .env.example .env                     # e preencha MISTRAL_API_KEY
uv run --env-file .env agents chat       # chat interativo (usa a API — ver aviso)
```

**Aviso (condição 4):** `agents chat` e qualquer `agent.run()` fazem chamadas de
modelo à API da Mistral e consomem a chave/quotas. Os testes do motor (`pytest`),
`agents --version` e `agents info` são locais e gratuitos. Só execute o chat
quando você autorizar o consumo.

## Permissões

- `permission_mode="ask"`: toda chamada de ferramenta espera aprovação humana.
- O agente não contata empresas, não publica nada e não faz deploy por conta própria.

## Regras do motor (resumo v2.5)

- **PC (0–100):** Porte 35 · Estrutura operacional 35 (exclusividade de fato,
  ordem B3→B2→B1; cadastro sem data = 0) · Investimento comprovado 30.
  Site/Instagram/seguidores/YouTube = inferência = 0. Alegação autodeclarada = 0.
- **OD (0–60):** itens com evidência obrigatória; ausência de site somente S3;
  cap 60; plataforma de terceiros nunca gera oportunidade automática.
- **QC (0–60):** tabela fechada; WhatsApp +20 só com identificação explícita
  pela própria empresa e titularidade confirmada; segundo telefone = 0.
- **CE = Cobertura × Qualidade média = Σw/7** (pesos 1,00/0,70/0,60/0,40/0,00).
- **Prioridade = floor((0,50×OD_n + 0,30×PC + 0,20×QC_n) × Fator_CE)**, 0–100.
- **Dados insuficientes:** fato crítico (E1/E2/E4/E5) não comprovado, CE < 50%,
  protocolo incompleto ou site em S2.

## Casos de referência (cobertos pelos testes)

| Caso | Estado do site | PC | OD | QC | CE | Prioridade | Classe |
|---|---|---|---|---|---|---|---|
| BODYFIT Estética | S1 | 10 | 0 | 40 | 77,1% | 13 Baixa | Oportunidade não identificada |
| El Shadai | S2 | 35 | 0 | 10 | 28,6% | 4 Muito baixa | Dados insuficientes |
| Taberna Delicatessen Delivery | S2 | 10 | 0 | 30 | 31,4% | 3 Muito baixa | Dados insuficientes |

## Condições desta entrega

- Branch `feat/kc-analista-comercial` — a `main` não foi alterada.
- Sem merge, deploy ou publicação.
- Sem chamadas pagas à API (nenhum teste executou o modelo).
