# KC Studio — Prospecção Comercial

Base comercial de prospecção da KC Studio: empresas com potencial para contratar criação de sites profissionais, priorizando a Baixada Fluminense e a Zona Oeste do Rio de Janeiro.

## Finalidade

Esta pasta centraliza a ferramenta de prospecção, acompanhamento e gestão comercial da KC Studio dentro do repositório kc-studio-arquivos1. A base atual contém **50 leads verificados em fontes públicas** (consulta de 15/11/2026), com evidências, pontuação, prioridade e uma mensagem de primeira abordagem personalizada para cada empresa.

O modelo comercial da KC Studio: identificar a empresa, contatar pelo WhatsApp, entender a necessidade, desenvolver uma **prévia personalizada** conforme o escopo definido, apresentar a prévia e, após aprovação e contratação, desenvolver e publicar o site.

## Estrutura

```
kc-studio-prospeccao/
├── README.md
├── leads-kc-studio.xlsx
└── docs/
    ├── criterios-de-prospeccao.md
    └── metodologia-de-pesquisa.md
```

## Como utilizar a planilha

O arquivo `leads-kc-studio.xlsx` tem quatro abas:

1. **LEADS** — base principal, com 26 colunas por empresa (identificação, contatos, situação digital, evidências, pontuação, abordagem personalizada e controle de pipeline). A primeira linha está congelada e há filtros automáticos em todas as colunas.
2. **INDICADORES** — painel com fórmulas vivas vinculadas à aba LEADS e ao histórico da aba ACOMPANHAMENTO. Recalcula sozinho.
3. **ACOMPANHAMENTO** — histórico comercial acumulativo. Um contato por linha, sempre em linha nova, sem apagar registros anteriores.
4. **CRITÉRIOS** — documentação da metodologia, pontuação, prioridades, regras de atualização e orientações de prospecção responsável.

## Como atualizar os leads

1. Cadastre novos leads na aba LEADS, na primeira linha vazia, seguindo o padrão de ID (KC-051, KC-052...).
2. Preencha apenas informações verificadas, com a URL da fonte e a data da verificação.
3. Classifique cada informação como FATO VERIFICADO, INFERÊNCIA ou HIPÓTESE (definições na aba CRITÉRIOS).
4. Não apague evidências nem abordagens antigas ao editar uma linha.
5. Use as listas suspensas das colunas Status da prospecção, Prioridade e Grau de confiança.

## Como interpretar os indicadores

- **Total cadastrado e % da meta**: acompanham o preenchimento da base (meta de 50).
- **Por cidade e por segmento**: mostram a distribuição geográfica e setorial; use para decidir onde pesquisar o próximo lote.
- **Sem site confirmado x ausência inferida**: separa o que a própria empresa declarou do que foi inferido pela pesquisa. Nunca trate ausência inferida como fato.
- **Prioridades**: contagem por faixa de pontuação (Alta 85-100, Média-alta 70-84, A investigar 50-69, Não priorizar <50).
- **Pipeline**: contatos, respostas, interessados, apresentações, prévias, propostas, contratos e taxa de conversão, todos calculados a partir dos status da aba LEADS e das linhas da aba ACOMPANHAMENTO.

## Como funciona a pontuação

| Critério | Pontos |
|---|---:|
| Necessidade ou problema digital verificável | 25 |
| Compatibilidade com os serviços da KC Studio | 20 |
| Momento comercial e sinais de oportunidade | 20 |
| Facilidade de contato empresarial | 15 |
| Qualidade das evidências | 20 |

Faixas: 85-100 prioridade alta; 70-84 média-alta; 50-69 oportunidade a investigar; abaixo de 50 não priorizar. Ausência de site não é prova de interesse nem de capacidade financeira.

## Como registrar novos contatos

1. Altere o status do lead na aba LEADS (ex.: de "Pronto para contato" para "Primeiro contato realizado") e preencha as datas.
2. Abra a aba ACOMPANHAMENTO e adicione uma linha nova com: ID do lead, empresa, data, tipo de atividade, canal, resultado, objeção (se houver), próxima ação e data do próximo acompanhamento.
3. Nunca sobrescreva linhas anteriores do histórico.
4. Cadência sugerida: follow-up em 48h sem resposta, segunda tentativa em 4 dias, encerramento do ciclo em 7 dias.

## Prospecção responsável

- Apenas dados empresariais publicamente disponíveis.
- Sem dados pessoais privados, listas compradas ou bases vazadas.
- Sem coleta indiscriminada; sem contorno de sistemas privados ou autenticações.
- Respeito à LGPD, registro de fonte e data, e respeito a pedidos de não contato (status "Não contatar").

## Contato

KC Studio — sites personalizados para pequenos e médios negócios. Canal comercial: WhatsApp.
