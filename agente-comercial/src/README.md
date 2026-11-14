# Entrada, saída e motor de pontuação — KC Studio

Implementação local em Python, sem API, IA, rede ou credenciais. Requer Python 3.10+ e usa apenas a biblioteca padrão.

## Executar testes

Na pasta `agente-comercial/src`:

```bash
python -m unittest discover -s ../tests -v
```

## Avaliar um registro JSON

Na pasta `agente-comercial/src`:

```bash
python data_io.py ../examples/SEU_ARQUIVO.json
```

Para salvar o relatório em arquivo:

```bash
python data_io.py ../examples/SEU_ARQUIVO.json --output ../reports/resultado.json
```

Use `examples/lead_input.template.json` como estrutura inicial. Faça uma cópia e preencha com dados de uma empresa real e evidências verificadas. O arquivo de modelo está deliberadamente vazio e **não representa um lead**.

## Contrato de entrada

O JSON deve conter:
- `business.name`, `business.city` e `business.segment`;
- objetos `pc`, `od`, `qc` e `ce`, conforme o modelo;
- evidências com `source_url` e `verified_on`; PC também exige `fact_id`, e CE exige `evidence_level`.

O relatório preserva os dados da empresa e retorna PC, OD, QC, CE, prioridade, status do funil, pendências e controles operacionais. A abordagem permanece bloqueada: `approach_allowed=false`.

## Limites

- Não pesquisa empresas, não acessa URLs e não verifica a veracidade das fontes.
- Não cria leads, contatos ou evidências.
- O operador deve conferir cada fonte e data.
- O motor aplica a pontuação aos dados informados; a revisão humana continua obrigatória.
