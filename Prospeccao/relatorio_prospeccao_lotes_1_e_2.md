# Relatório de Prospecção — KC Studio
## Lotes 1 e 2 · Duque de Caxias – RJ · Verificado em 2026-11-14

## 1. Resumo executivo

- **Base recuperada sem nova pesquisa:** 24 leads reais do CRM anterior (`CRM/KC_Studio_CRM_Demonstracao.xlsx`, excluindo 3 linhas de demonstração com telefones fictícios) + 50 leads do PR #2 (`CRM/KC_Studio_CRM_50_Leads_Duque_de_Caxias.xlsx`). Total de 74 leads já registrados, usados para evitar duplicatas.
- **14 empresas investigadas individualmente** nos dois lotes, cada uma com evidência verificada por URL e data.
- **Resultado consolidado:** 8 leads no Grupo A (abordagem liberada), 6 no Grupo B (mensagem pronta ou pendente de leitura complementar), **0 no Grupo C** — as duas empresas que estavam com dados insuficientes no Lote 1 (URBZ e Jomasa) foram reanalisadas e promovidas no Lote 2.
- **Achados de maior valor:**
  - **Art Dentista:** o domínio principal da clínica (artdentista.com.br) está **fora do ar** (erro "Não há VirtualHost configurado") — quem digita o endereço principal não chega à clínica, que opera por um domínio secundário completo.
  - **CESOP:** site moderno com nota 4,9 e 563 avaliações do Google exibidas na home, mas com contadores zerados ("0 m²", "0 %") e título do FAQ corrompido ("Qua a sual?").
  - **Jomasa Imóveis:** nome corrompido no Google ("Jomasa Imï¿½veis") + banner da época da COVID-19 ainda na página inicial.
  - **LMS Consultoria Imobiliária (Lote 1):** codificação corrompida no site ("ImÃ³vel").

## 2. Skills e ferramentas realmente utilizadas

| Item | Status |
|---|---|
| Skill `kc-studio-sales-intelligence` | Ativada (lida na íntegra do registro Mistral) |
| Skill `goskil` | Ativada (lida na íntegra; termina truncada no critério "0–29") |
| Skill `file-creator` | Ativada (lida na íntegra) |
| Pesquisa web (buscas) | Utilizada — evidências por URL em cada ficha |
| Leitura/análise de sites | Utilizada — 4 sites lidos integralmente (LMS, Feital, CESOP, Art Dentista/domínio secundário); URBZ e Jomasa bloquearam leitura direta (conteúdo confirmado via resultados de busca); OdontoArêas e NeoRiso com leitura direta falha (serviço de fetch indisponível / página dependente de JS) |
| Análise de redes sociais | Utilizada via resultados de busca (Instagram/Facebook públicos) — perfis não navegados internamente |
| Criação de planilha | Utilizada — openpyxl (Python), arquivo validado ao reabrir |
| Envio de mensagens / ligações | Não executado (regra da operação) |

## 3. Metodologia de classificação (transparência sobre a v2.5)

**A metodologia v2.5 oficial não foi encontrada no workspace**: nenhuma das 3 skills do registro define S1–S4, PC, OD, QC ou CE, e a skill `goskil` termina truncada. Para não travar a operação, os rótulos foram aplicados com critérios explícitos abaixo. **Os fatos, evidências e mensagens não dependem dessa escolha** — ao receber o documento oficial v2.5, os campos são reclassificados sem alterar dados.

| Rótulo | Critério adotado |
|---|---|
| S1 | Sem site próprio; depende de redes sociais ou plataformas de terceiros |
| S2 | Site próprio com defeitos de apresentação (ex.: codificação, conteúdo quebrado, domínio fora do ar) |
| S3 | Site próprio funcional, porém genérico/template sem apresentação institucional |
| S4 | Presença digital madura (nenhuma empresa dos lotes) |
| PC | Potencial Comercial: Alto / Médio / Baixo (porte, múltiplas unidades, receita de serviços) |
| OD | Oportunidade Digital: Alta / Média / Baixa — sempre com justificativa verificável |
| QC | Qualidade de Contato: Confirmado / Parcial / Pendente |
| CE | Capacidade estimada de investimento, baseada em evidências observadas |
| Score 0–100 | Critérios das skills da KC Studio (ausência/qualidade de site, presença digital, potencial do segmento, capacidade aparente, facilidade de contato com decisor, oportunidade clara) |

## 4. Empresas verificadas — diagnóstico individual

### Grupo A — Melhor oportunidade (abordagem liberada) — 8 empresas

**A1. Art Dentista** — Clínica odontológica, Centro · **Score 78**
- S2 · PC Alto · OD Alta · QC Confirmado · CE Médio/Alta
- **Fatos:** fundada em 2002; sócias Dra. Amanda Dias (Prótese e Implantodontia) e Dra. Jennifer Rodrigues (Periodontia e Implantodontia); tel. (21) 99094-9915; R. Mariano Sendra dos Santos, 88, sl. 104; nota 4,9 (156 avaliações no DentMap); blog ativo.
- **Oportunidade:** domínio principal artdentista.com.br **fora do ar** (erro de VirtualHost, verificado em 2026-11-14); no site ativo, itens 02 e 03 da seção de diferenciais com texto idêntico.
- **Fontes:** dentistaemduquedecaxias.com.br (lido integralmente); artdentista.com.br (erro); dentmap.com.br; facebook.com/ArtDentista.

**A2. CESOP — Clínica Espaço Saúde Oral Plena** — Clínica odontológica, Jardim 25 de Agosto · **Score 75**
- S2 · PC Alto · OD Alta · QC Confirmado · CE Alta
- **Fatos:** site lido integralmente; 6 especialidades; nota 4,9 com 563 avaliações do Google exibidas; tel. (21) 2771-1725 e (21) 98401-2771; Av. Brigadeiro Lima e Silva, 1963, SL 302.
- **Oportunidade:** contadores da home zerados ("0 m²", "0 %", "1 Anos de Experiência") e título do FAQ corrompido ("Qua a sual?").
- **Fontes:** clinicacesop.com.br (lido integralmente, 2026-11-14).

**A3. LMS Consultoria Imobiliária (CRECI 11603)** — Imobiliária, Jardim Vinte e Cinco de Agosto · **Score 70**
- S2 · PC Alto · OD Alta · QC Confirmado · CE Médio/Alta
- **Fatos:** site lido integralmente; busca por 16 bairros; CRECI 11603; tel. (21) 99358-2358.
- **Oportunidade:** codificação corrompida ("ImÃ³vel", "vocÃª") em títulos do site; template genérico.
- **Fontes:** leticiamartinsimoveis.com.br (lido 2026-11-14); CRM KC Studio.

**A4. Jomasa Imóveis (CRECI J 2634)** — Imobiliária, Jardim Vinte e Cinco de Agosto · **Score 70**
- S2 · PC Alto · OD Alta · QC Confirmado · CE Média
- **Fatos:** Rua Marechal Deodoro, 557, salão 201; tel. (21) 2671-1770 / (21) 2671-0405; e-mail locacao@jomasaimoveis.com; Instagram @jomasaimoveis; página própria de 2ª via de boleto.
- **Oportunidade:** nome corrompido em resultado de busca ("Jomasa Imï¿½veis") + banner da COVID-19 ainda na home.
- **Pendência:** leitura direta bloqueada — conteúdo confirmado via resultados de busca.
- **Fontes:** resultados de busca com conteúdo de jomasaimoveis.com (2026-11-14); CRM KC Studio.

**A5. Feital Imóveis (CRECI 5540-0)** — Imobiliária · **Score 70**
- S3 · PC Alto · OD Média · QC Confirmado · CE Média
- **Fatos:** site lido integralmente; buscador com filtros; tel. (21) 2671-5150 / WhatsApp (21) 96773-5150.
- **Oportunidade:** home sem apresentação institucional (história, equipe, CRECI, prova social).
- **Fontes:** feitalimoveis.com.br (lido 2026-11-14); CRM KC Studio.

**A6. NeoRiso Odontologia (CRO-RJ 31027)** — Clínica odontológica, 25 de Agosto/Centro · **Score 68**
- S2 · PC Alto · OD Média · QC Confirmado · CE Médio/Alta
- **Fatos:** CNPJ 24.419.086/0001-50 (fundada 18/03/2016); tel. (21) 2771-0312 (Facebook, 1.338 curtidas); 17 anos de atuação; Dr. Felipe Martins citado em avaliações do site.
- **Oportunidade:** rodapé com placeholder "CRO: xxxxxxxx" em parte das páginas; endereço do site (Mal. Deodoro, 392) diverge do CNPJ/Waze (Av. Perimetral Mal. Deodoro, 557).
- **Pendência:** home depende de vídeo/JS e não abriu na leitura direta.
- **Fontes:** neoriso.com.br via resultados de busca; facebook.com/clinicaneoriso; econodata; waze (2026-11-14).

**A7. BarBelo Barbearia** — Barbearia, 25 de Agosto · **Score 65**
- S1 · PC Médio · OD Alta · QC Confirmado · CE Média
- **Fatos:** Instagram @barbelobarbershop (1.352 seguidores) com 2 telefones na bio; Facebook (2.078 curtidas) com vídeo institucional.
- **Oportunidade:** bio menciona agendamento "pelo nosso site", mas não há site próprio identificado.
- **Fontes:** instagram.com/barbelobarbershop; facebook.com/barbelobarbershop (2026-11-14); CRM KC Studio.

**A8. R&B Barbearia** — Barbearia · **Score 65**
- S1 · PC Médio · OD Alta · QC Confirmado · CE Baixo/Médio
- **Fatos:** WhatsApp +55 21 98783-0127 publicado na página oficial do Facebook.
- **Oportunidade:** dependência total de uma única rede social.
- **Fontes:** facebook.com/rebbarbearia (2026-11-14); CRM KC Studio.

### Grupo B — Potencial comercial — 6 empresas

**B1. Barbearia Novo Visual** — S1 · Score 70 · Instagram @novovisualcleytonbarbeiros (5.114 seguidores)
- Fatos: 3 unidades em Duque de Caxias; curso de barbeiro.
- Oportunidade: operação multi-unidade + curso exige site institucional.
- Pendências: **nenhum contato publicado**; **risco de homônimos** — existem negócios de mesmo nome em Goiânia e Teófilo Otoni/MG com sites próprios (ex.: barbearianovovisual.com.br); esses domínios/telefones NÃO podem ser atribuídos à Novo Visual de Caxias sem confirmação.
- Fonte: instagram.com/novovisualcleytonbarbeiros (2026-11-14).

**B2. OdontoArêas** — S3 · Score 60 · Xerém (Estrada Rio D'ouro, 1040)
- Fatos: Dr. Luiz Carlos Martins Arêas formado em 1992; consultório em 2013, clínica ampliada em 2022; corpo clínico multidisciplinar; diferenciais: hipnose clínica e urgência/emergência.
- Pendências: **telefone não localizado**; leitura direta do site falhou 2x — mensagem será gerada somente após a leitura completa.
- Fonte: odontoareas.com.br via resultados de busca (2026-11-14).

**B3. URBZ Imobiliária (CRECI J-7683)** — S3 · Score 60 · Jardim Vinte e Cinco de Agosto
- Fatos: fundada em 2017 por Bruno Pinto e Alcimar Pinto; venda, locação, administração e legalização; assistente virtual "Bruno Assistente URBZ"; WhatsApp nos imóveis; tel. (21) 3135-5135 / (21) 96892-4776.
- Oportunidade: site aparentemente maduro; leitura direta bloqueada por verificação de segurança impede avaliar experiência mobile — mensagem cobre apenas o que foi observado.
- **Reclassificada do Grupo C para o Grupo B no Lote 2.**
- Fontes: resultados de busca com conteúdo de urbzimobiliaria.com.br (2026-11-14); CRM KC Studio.

**B4. Walker's Barber Shop** — S1 · Score 60 · Parque Senhor do Bonfim / Parque Boa Vista I
- Fatos: desde Outubro/2016; CNPJ com matriz e filial, capital social R$ 218 mil; visagismo e próteses capilares; Instagram (2.101 seguidores, 867 posts) e Facebook (2.237 curtidas).
- Pendência: **contato não publicado**; 2 endereços a confirmar.
- Fontes: instagram.com/walkersbarbershoprj; facebook.com/walkersbarbearia; econodata; Solutudo (2026-11-14).

**B5. Carol Miller Barbearia** — S1 · Score 52 · Instagram @carolmillerbarbearia (2.796 seguidores)
- Fatos: atendimento adultos e kids; agendamento online já operando via Booksy (plataforma paga); Facebook (519 curtidas).
- Pendência: **contato não publicado**.
- Fontes: instagram.com/carolmillerbarbearia; facebook.com/carolmillerbarbearia; Booksy (2026-11-14).

**B6. Barbershop do Alex** — S1 · Score 50 · Rua Tenente José Dias, 153
- Fatos: diferencial de experiência (PS4, cerveja gelada); horário fixo; bio convoca "Chama no WhatsApp!" sem número público.
- Pendência: **número de WhatsApp não publicado**.
- Fonte: instagram.com/barbershop_doalex (2026-11-14).

### Grupo C — Dados insuficientes (SEM abordagem comercial)

**Nenhuma empresa neste momento.** URBZ e Jomasa, que estavam no Grupo C ao fim do Lote 1, foram reanalisadas no Lote 2 e promovidas (URBZ → B, Jomasa → A) com base em conteúdo confirmado em resultados de busca.

## 5. Mensagens personalizadas (WhatsApp)

13 mensagens prontas na planilha, coluna **"Mensagem personalizada WhatsApp"** (8 do Grupo A + 5 do Grupo B; a OdontoArêas fica sem mensagem até a leitura do site). Estrutura aplicada em todas: identificação e contexto → reconhecimento específico com fato verificado → demonstração de conhecimento → oportunidade → pergunta de abertura. Nenhuma mensagem oferece prévia gratuita no primeiro contato, nenhuma promete resultado e nenhuma afirma ter acessado o que não acessou — quando a leitura direta do site foi bloqueada (URBZ, Jomasa), a mensagem descreve exatamente o que foi observado e por qual meio.

## 6. Resumo quantitativo

| Indicador | Valor |
|---|---|
| Leads anteriores recuperados (sem nova pesquisa) | 74 (24 reais do CRM + 50 do PR #2) |
| Empresas investigadas individualmente (Lotes 1 e 2) | 14 |
| — Lote 1 | 10 empresas |
| — Lote 2 | 10 empresas (4 novas + 6 reclassificadas/atualizadas) |
| Grupo A (abordagem liberada) | 8 |
| Grupo B (potencial comercial) | 6 |
| Grupo C (dados insuficientes) | 0 |
| Mensagens personalizadas prontas | 13 |
| Contatos confirmados | 10 |
| Sites lidos integralmente | 4 (LMS, Feital, CESOP, Art Dentista/domínio secundário) |
| Sites com leitura direta bloqueada/falha | 4 (URBZ, Jomasa, OdontoArêas, NeoRiso/home) |
| Empresas duplicadas entre lotes | 0 |

## 7. Próximos passos (Lote 3)

1. **Segmentos ainda não cobertos:** clínicas médicas, clínicas de estética, academias, construtoras, restaurantes e escritórios de advocacia.
2. **Fila de leads já identificados (verificar antes de classificar):**
   - Odontologia: Novo Sorriso Odontologia (Nova Campinas, tel. (21) 2776-4244, sem site próprio identificado), Odonto e Cia Caxias ((21) 2673-9231), Odontostar Caxias ((21) 98507-3151, site em plataforma codental.site), Clínica Odonto House (Rua Marechal Bento Manoel, 373), Sorria Bem (Av. Duque de Caxias, 149).
   - Barbearias: Barbearia do Mendes (WhatsApp (21) 98222-7447), WD Salão e Barbearia ((21) 2673-2432), SCarla Barbearia (WhatsApp +55 21 97513-2993), Barbearia 25 (2.708 curtidas no Facebook), Bate Papo Chopperia, Salão So Vitória (17 anos no mesmo endereço).
3. **Pendências do Lote 2:** ler diretamente os sites de URBZ, Jomasa, OdontoArêas e NeoRiso (método alternativo) e localizar contatos de Novo Visual, Walker's, Carol Miller e Barbershop do Alex.
4. Reaplicar rótulos oficiais v2.5 quando o documento for disponibilizado.
