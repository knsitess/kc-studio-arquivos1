# KC Studio — Analista Comercial

Agente de inteligência comercial para localizar empresas reais, verificar presença digital, qualificar oportunidades e preparar abordagens personalizadas.

## Estado do projeto

- Metodologia de avaliação: v2.5 congelada.
- Implementação: motor determinístico de pontuação criado em `src/scoring.py`; testes automatizados em `tests/test_scoring.py`.
- Validação local dos testes: ainda pendente; executar conforme `src/README.md`.
- Provedor de modelo, ferramenta de pesquisa e ambiente de execução: ainda a definir e validar.
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

- `metodologia/metodologia-v2.5.md`: regras congeladas de avaliação.
- `src/`: implementação do agente (a definir após validar SDK, ferramentas e ambiente).
- `skills/`: instruções especializadas e fluxos operacionais.
- `config/`: configuração sem credenciais.
- `tests/`: casos de teste e validação.

## Próximas etapas

1. Definir e validar o ambiente de execução e o SDK do modelo.
2. Escolher uma fonte de pesquisa verificável e implementar coleta com registro de evidências.
3. Executar e corrigir os testes locais do motor de pontuação.
4. Implementar entrada/saída de dados e registro de evidências.
5. Escolher fonte de pesquisa verificável e integrar coleta automatizada.
6. Só então conectar interface ou fluxo de operação.

## Segurança de configuração

Nunca commitar chaves de API, tokens, cookies ou credenciais. Use variáveis de ambiente no ambiente de execução. O arquivo `.env.example` deve conter apenas nomes de variáveis e valores fictícios claramente identificados.
