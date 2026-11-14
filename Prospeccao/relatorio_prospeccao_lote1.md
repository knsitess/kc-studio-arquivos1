# Relatório de Prospecção — KC Studio
## Lote 1 · Duque de Caxias – RJ · Verificado em 2026-11-14

## 1. Resumo executivo

- **Base recuperada sem nova pesquisa:** 24 leads reais do CRM anterior (`CRM/KC_Studio_CRM_Demonstracao.xlsx`, excluindo 3 linhas de demonstração com telefones fictícios) + 50 leads do PR #2 (`CRM/KC_Studio_CRM_50_Leads_Duque_de_Caxias.xlsx`). Total de 74 leads já registrados, usados para evitar duplicatas.
- **Lote 1 investigado individualmente:** 10 empresas (imobiliárias, barbearias e clínicas odontológicas priorizadas), cada uma com evidência verificada por URL e data.
- **Resultado do lote:** 4 leads no Grupo A (abordagem liberada), 4 no Grupo B (mensagem pronta, contato pendente de confirmação), 2 no Grupo C (dados insuficientes, sem abordagem).
- **Achado de maior valor:** a LMS Consultoria Imobiliária tem site próprio com codificação de caracteres corrompida visível ("ImÃ³vel" em vez de "Imóvel") — oportunidade concreta e demonstrável em uma imobiliária com CRECI ativo e escritório na Av. Brigadeiro Lima e Silva.

## 2. Skills e ferramentas realmente utilizadas

| Item | Status |
|---|---|
| Skill `kc-studio-sales-intelligence` | Ativada (lida na íntegra do registro Mistral) |
| Skill `goskil` | Ativada (lida na íntegra; termina truncada no critério "0–29") |
| Skill `file-creator` | Ativada (lida na íntegra) |
| Pesquisa web (buscas) | Utilizada — evidências por URL em cada ficha |
| Leitura/análise de sites | Utilizada — 2 sites lidos integralmente (LMS, Feital); 2 bloqueados (URBZ, Jomasa) |
| Análise de redes sociais | Utilizada via resultados de busca (Instagram/Facebook públicos) — perfis não navegados internamente |
| Criação de planilha | Utilizada — openpyxl (Python), arquivo validado ao reabrir |
| Envio de mensagens / ligações | Não executado (regra da operação) |

## 3. Metodologia de classificação (transparência sobre a v2.5)

**A metodologia v2.5 oficial não foi encontrada no workspace**: nenhuma das 3 skills do registro define S1–S4, PC, OD, QC ou CE, e a skill `goskil` termina truncada. Para não travar a operação, os rótulos foram aplicados com critérios explícitos abaixo. **Os fatos, evidências e mensagens não dependem dessa escolha** — ao receber o documento oficial v2.5, os campos são reclassificados sem alterar dados.

| Rótulo | Critério adotado |
|---|---|
| S1 | Sem site próprio; depende de redes sociais ou plataformas de terceiros |
| S2 | Site próprio com defeitos de apresentação (ex.: codificação, conteúdo quebrado) |
| S3 | Site próprio funcional, porém genérico/template sem apresentação institucional |
| S4 | Presença digital madura (nenhuma empresa do lote) |
| PC | Potencial Comercial: Alto / Médio / Baixo (porte, múltiplas unidades, receita de serviços) |
| OD | Oportunidade Digital: Alta / Média / Baixa — sempre com justificativa verificável |
| QC | Qualidade de Contato: Confirmado / Parcial / Pendente |
| CE | Capacidade estimada de investimento, baseada em evidências observadas |
| Score 0–100 | Critérios das skills da KC Studio (ausência/qualidade de site, presença digital, potencial do segmento, capacidade aparente, facilidade de contato com decisor, oportunidade clara) |

## 4. Empresas verificadas — diagnóstico individual

### Grupo A — Melhor oportunidade (abordagem liberada)

**A1. LMS Consultoria Imobiliária (CRECI 11603)** — Imobiliária, Jardim Vinte e Cinco de Agosto
- S2 · PC Alto · OD Alta · QC Confirmado · CE Média/Alta · Score 70 (alta prioridade)
- **Fatos comprovados:** site ativo com busca por bairros (16 regiões), seção "A Empresa", simulação de financiamento; CRECI 11603; Av. Brigadeiro Lima e Silva, 1951 sala 301; tel. (21) 99358-2358; e-mail lmsconsultoriaimob@gmail.com.
- **Oportunidade:** codificação de caracteres corrompida em títulos do site ("ImÃ³vel", "vocÃª") — verificado na leitura de 2026-11-14. Template genérico "Site para Imobiliarias".
- **Inferências:** escritório em via comercial principal → capacidade de investimento real.
- **Pendências:** redes sociais oficiais; mantenedor do template.
- **Fontes:** https://leticiamartinsimoveis.com.br (lido 2026-11-14); CRM KC Studio.

**A2. Feital Imóveis (CRECI 5540-0)** — Imobiliária
- S3 · PC Alto · OD Média · QC Confirmado · CE Média · Score 70 (alta prioridade)
- **Fatos comprovados:** site ativo com buscador (comprar/alugar, filtros de bairro e quartos), destaques e lançamentos; telefone (21) 2671-5150 e WhatsApp (21) 96773-5150 (verificação anterior).
- **Oportunidade:** página inicial sem apresentação institucional (história, equipe, CRECI, prova social); template "Universal Software".
- **Pendências:** endereço físico atual; redes sociais.
- **Fontes:** https://feitalimoveis.com.br (lido 2026-11-14); CRM KC Studio.

**A3. BarBelo Barbearia** — Barbearia, 25 de Agosto
- S1 · PC Médio · OD Alta · QC Confirmado · CE Média · Score 65 (oportunidade moderada)
- **Fatos comprovados:** Instagram @barbelobarbershop (1.352 seguidores, 363 posts) com endereço e 2 telefones na bio; Facebook com 2.078 curtidas e vídeo institucional; conceito "tradição e modernidade".
- **Oportunidade:** bio menciona agendamento "pelo nosso site", mas não há site próprio identificado — provável link de terceiros (a confirmar).
- **Pendências:** destino do link "nosso site" da bio.
- **Fontes:** instagram.com/barbelobarbershop; facebook.com/barbelobarbershop (2026-11-14); CRM KC Studio.

**A4. R&B Barbearia** — Barbearia
- S1 · PC Médio · OD Alta · QC Confirmado · CE Baixa/Média · Score 65 (oportunidade moderada)
- **Fatos comprovados:** WhatsApp +55 21 98783-0127 publicado na página oficial do Facebook (facebook.com/rebbarbearia).
- **Oportunidade:** dependência total de uma única rede social; sem canal próprio.
- **Pendências:** endereço; Instagram oficial.
- **Fontes:** facebook.com/rebbarbearia (2026-11-14); CRM KC Studio.

### Grupo B — Potencial comercial (mensagem pronta; contato a confirmar)

**B1. Barbearia Novo Visual** — S1 · Score 70 · Instagram @novovisualcleytonbarbeiros (5.114 seguidores)
- Fatos: 3 unidades em Duque de Caxias; curso de barbeiro; posicionamento "ajudamos na autoestima".
- Oportunidade: operação multi-unidade + curso exige site institucional (unidades, grade, inscrição).
- Pendência: **nenhum contato publicado** — localizar telefone/WhatsApp oficial antes do envio.
- Fonte: instagram.com/novovisualcleytonbarbeiros (2026-11-14).

**B2. Walker's Barber Shop** — S1 · Score 55 · Instagram @walkersbarbershoprj (2.101 seguidores, 867 posts)
- Fatos: desde Outubro/2016; especialistas em visagismo e próteses capilares; horário até 22h.
- Oportunidade: especialidades invisíveis no Google por falta de site indexável.
- Pendência: **contato não publicado**.
- Fonte: instagram.com/walkersbarbershoprj (2026-11-14).

**B3. Carol Miller Barbearia** — S1 · Score 50 · Instagram @carolmillerbarbearia (2.796 seguidores, 269 posts)
- Fatos: atendimento adultos e kids; marca construída na profissional @carolbarber.rj.
- Pendência: **contato não publicado**.
- Fonte: instagram.com/carolmillerbarbearia (2026-11-14).

**B4. Barbershop do Alex** — S1 · Score 50 · Instagram @barbershop_doalex (960 seguidores)
- Fatos: Rua Tenente José Dias, 153; diferencial de experiência (PS4, cerveja gelada); WhatsApp citado sem número público.
- Pendência: **número de WhatsApp não publicado**.
- Fonte: instagram.com/barbershop_doalex (2026-11-14).

### Grupo C — Dados insuficientes (SEM abordagem comercial)

**C1. URBZ Imobiliária (CRECI J-7683)** — site responde apenas página de verificação de segurança (Cloudflare); conteúdo não analisável nesta tentativa. Pendência: reanalisar. Telefones de verificação anterior: (21) 3135-5135 / (21) 96892-4776.

**C2. Jomasa Imóveis** — domínio respondeu mas bloqueou leitura automatizada. Pendência: reanalisar. Telefones de verificação anterior: (21) 2671-1770 / (21) 2671-0405.

## 5. Mensagens personalizadas (WhatsApp)

As 8 mensagens (A1–A4, B1–B4) estão na planilha, coluna **"Mensagem personalizada WhatsApp"**. Estrutura aplicada em todas: identificação e contexto → reconhecimento específico com fato verificado → demonstração de conhecimento → oportunidade → pergunta de abertura. Nenhuma mensagem oferece prévia gratuita no primeiro contato, nenhuma promete resultado e nenhuma afirma ter acessado o que não acessou (perfis de Instagram/Facebook verificados via resultados públicos de busca; sites lidos integralmente quando a leitura foi possível).

## 6. Resumo quantitativo

| Indicador | Valor |
|---|---|
| Leads anteriores recuperados (sem nova pesquisa) | 74 (24 reais do CRM + 50 do PR #2) |
| Empresas investigadas individualmente no Lote 1 | 10 |
| Grupo A (abordagem liberada) | 4 |
| Grupo B (potencial comercial, contato pendente) | 4 |
| Grupo C (dados insuficientes, sem abordagem) | 2 |
| Mensagens personalizadas prontas | 8 |
| Contatos confirmados | 6 |
| Sites lidos integralmente | 2 (LMS, Feital) |
| Sites bloqueados para análise | 2 (URBZ, Jomasa) |
| Empresas duplicadas entre lotes | 0 |

## 7. Próximos passos (Lote 2)

1. Reanalisar URBZ e Jomasa por método alternativo para promovê-las do Grupo C.
2. Localizar contatos das 4 barbearias do Grupo B (Instagram cites WhatsApp em 2 casos).
3. Expandir para os segmentos ainda não cobertos no lote: clínicas médicas, clínicas de estética, academias, construtoras e restaurantes (odontológicas já mapeadas: CESOP, OdontoArêas, NeoRiso, Art Dentista — todas com site próprio, a investigar no Lote 2 antes de qualificar).
4. Reaplicar rótulos oficiais v2.5 quando o documento for disponibilizado.
