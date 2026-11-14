# Motor de pontuação — KC Studio

Implementação inicial e determinística da metodologia v2.5. Não usa API, IA, rede ou credenciais.

## Requisitos
Python 3.10 ou superior. Apenas biblioteca padrão.

## Executar testes
Na pasta `agente-comercial/src`:

```bash
python -m unittest discover -s ../tests -v
```

## Contrato de entrada
As funções recebem dicionários Python. Evidências que pontuam precisam conter `source_url`, `verified_on`, `fact_id` (PC) e `evidence_level` (CE). Campos ausentes, sem fonte ou sem data não pontuam. O motor calcula indicadores, mas **nunca autoriza abordagem**. A decisão de contato permanece humana.

## Limites desta primeira versão
- Não pesquisa empresas nem verifica URLs automaticamente.
- Não valida se a fonte realmente sustenta o fato; isso continua sendo revisão humana.
- Os valores PC devem ser informados conforme os critérios da metodologia.
- B3 vale 15 pontos no total e exige pelo menos duas unidades com evidência individual.
- Cobertura e qualidade média são calculadas separadamente; CE é o produto das duas.
- Dados insuficientes bloqueiam a entrada no funil ativo.
