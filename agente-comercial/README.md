# KC Studio — Analista Comercial

Agente de inteligência comercial para localizar empresas reais, verificar presença digital, qualificar oportunidades e preparar abordagens personalizadas.

## Estado do projeto

- Metodologia de avaliação: v2.5 congelada.
- Motor determinístico: `src/scoring.py`.
- Entrada e saída JSON: `src/data_io.py`.
- Modelo vazio de registro: `examples/lead_input.template.json` (não é lead real).
- Testes automatizados: `tests/`; execução local confirmada anteriormente para os 10 testes do motor de pontuação. Os novos testes de entrada/saída ainda precisam ser executados.
- Pesquisa automatizada, coleta de evidências e interface ainda não implementadas.
- Nenhum lead fictício deve ser criado.
- Nenhuma mensagem deve ser enviada automaticamente.

## Princípios obrigatórios

1. **Evidência antes de pontuação:** toda afirmação factual deve registrar informação, fonte e data de comprovação.
2. **Separar fato, inferência e pendência:** nunca apresentar inferência como fato confirmado.
3. **Rastreabilidade:** preservar URLs, datas, trechos/evidências e motivo da classificação.
4. **Bloqueio por dados insuficientes:** leads nessa condição não recebem mensagem de abordagem e ficam fora do funil ativo.
5. **Aprovação humana:** o agente prepara análises e mensagens; não envia mensagens, publica conteúdo, contrata serviços ou altera dados externos sem aprovação explícita.
6. **Sem fabricação:** não inventar empresas, contatos, sites, resultados de pesquisa ou evidências.
7. **Proteção de dados:** coletar apenas dados empresariais públicos necessários à finalidade comercial.

## Estrutura

- `metodologia/metodologia-v2.5.md`: regras congeladas.
- `src/scoring.py`: motor determinístico.
- `src/data_io.py`: leitura de entrada JSON e geração de relatório JSON.
- `examples/lead_input.template.json`: modelo vazio, sem empresa fictícia.
- `tests/`: testes automatizados.

## Próximas etapas

1. Executar os novos testes de entrada/saída no computador.
2. Corrigir eventuais falhas e validar com um registro real fornecido pelo operador.
3. Definir fonte de pesquisa verificável e implementar coleta com registro de evidências.
4. Só então integrar pesquisa automatizada e interface operacional.

## Segurança

Nunca commitar chaves de API, tokens, cookies ou credenciais. O fluxo atual não exige Mistral nem qualquer serviço pago.
