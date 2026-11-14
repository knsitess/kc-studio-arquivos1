# Metodologia v2.5 — KC Studio — Analista Comercial

**Status:** congelada para implementação.  
**Data de referência registrada no documento de origem:** 14/11/2026 (não confirmada externamente).  
**Regra de governança:** não reabrir revisão teórica. Corrigir apenas problemas operacionais concretos, documentando a alteração e sua justificativa.

## 1. Evidência e fontes

- Fato = informação + fonte + data de comprovação.
- A mesma tríade pontua no máximo uma vez no PC.
- Alegação autodeclarada: 0 pontos; registrar apenas como contexto.
- Deduplicar fontes repetidas e considerar o melhor peso aplicável.
- Fonte bloqueada: peso 0, não comprova.
- Snippet legível: peso 0,40.
- Distinguir explicitamente fato confirmado, inferência e pendência.
- Não criar leads fictícios nem completar lacunas por suposição.

## 2. Estado do site

| Estado | Definição |
|---|---|
| S1 | Site próprio confirmado: domínio próprio, conteúdo acessado diretamente e vínculo com a empresa comprovado. |
| S2 | Site candidato: titularidade/vínculo pendente; qualquer candidato relevante sem resolução mantém S2. |
| S3 | Site próprio não localizado: três buscas literais completas e todos os candidatos relevantes descartados com evidência documentada; candidato pendente impede S3. |
| S4 | Verificação incompleta. |

S2 e S3 são mutuamente exclusivos.

## 3. PC — Porte (0–100)

### A. Porte (35)
- Anos de atividade com fonte independente: 15.
- CNPJ ativo: 10.
- Endereço: 10.

### B. Estrutura operacional (35)
- B1: operação atual com data: 10.
- B2: atividade recente de terceiros, até 12 meses: 10.
- B3: múltiplas unidades: 15; cada unidade precisa de comprovação própria B1/B2.
- Critérios disjuntos; aplicar exclusividade na ordem B3 → B2 → B1.
- O mesmo fato não pode pontuar duas vezes.
- Endereço (A) e operação (B1) são fatos distintos, mesmo que apareçam na mesma fonte.
- Listagem/diretório/cadastro sem data não comprova operação atual.

### C. Investimento comprovado (30)
- Infraestrutura digital própria: 10 (não inclui plataforma de terceiros).
- Marketing pago comprovado: 10.
- Investimento documentado: 10.

Site, Instagram, seguidores e YouTube, isoladamente, são inferências e pontuam 0.

### Segmento
- A: saúde/estética/imobiliário/jurídico.
- B: academias/food/serviços.
- C: comércio local.

O segmento é camada estratégica para desempate e personalização; não pontua no PC.

## 4. OD — Oportunidade digital (0–60)

- Ausência de site, somente em S3: 10.
- S4: 5 pontos com duas buscas; 0 com uma busca ou menos.
- Invisibilidade testada: 10.
- Conversão constatada: 10.
- Desempenho medido: 10.
- Redesign constatado: 10.
- Funcionalidade ausente: 10.
- Deficiência constatada em página de plataforma, com acesso direto: 10.
- Teto: 60.
- Sem evidência: 0.
- Plataforma nunca gera oportunidade automática.

## 5. QC — Qualidade do contato (0–60)

- Canal oficial direto: 40.
- WhatsApp explicitamente identificado pela própria empresa: +20.
- Diretório com acesso direto: 30.
- DM: 15.
- Snippet legível: 10.
- Snippet truncado: 5.
- Bloqueado: 0.
- Segundo telefone: 0.
- Titularidade não confirmada nunca recebe bônus.

## 6. CE — Confiabilidade da evidência

CE = Cobertura × Qualidade média = Σw/7.

Sete fatos essenciais E1–E7; pesos:
- 1,00: oficial direto.
- 0,70: oficial snippet.
- 0,60: base cadastral/diretório direto.
- 0,40: snippet legível.
- 0,00: bloqueado.

Registrar Cobertura e Qualidade separadamente.

Fatores:
- CE ≥80%: fator 1,00.
- CE 50–79%: fator 0,85.
- CE 35–49%: fator 0,60 + Dados Insuficientes (DI).
- CE <35%: fator 0,30 + DI.

Fatos críticos: E1 existência/operação; E2 segmento; E4 contato publicado; E5 status de presença digital.  
Complementares: E3 endereço; E6 titularidade do contato; E7 CNPJ ativo.

### Dados insuficientes

Marcar DI quando qualquer fato crítico E1/E2/E4/E5 não estiver comprovado, CE <50%, protocolo incompleto ou site S2 sem resolução.

Obrigações:
- Registrar fatos faltantes.
- Registrar a próxima verificação específica.
- Não gerar mensagem de abordagem.
- Manter fora do funil ativo, com status “Pendente de verificação”.

## 7. Prioridade

`Prioridade = floor((0,50 × OD_n + 0,30 × PC_n + 0,20 × QC_n) × Fator_CE)`

- OD_n = OD/60 × 100.
- QC_n = QC/60 × 100.
- PC já está na escala 0–100.
- Teto: 100.

Faixas:
- Alta: ≥60.
- Média: 40–59.
- Moderada: 20–39.
- Baixa: 5–19.
- Muito baixa: <5.

## 8. Casos de referência da versão congelada

| Empresa | Site | PC | OD | QC | CE | Fator CE | Prioridade | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| BODYFIT Estética | S1 | 10 | 0 | 40 | 77,1% | 0,85 | 13 | Oportunidade não identificada |
| El Shadai | S2 | 35 | 0 | 10 | 28,6% | 0,30 | 4 | Dados insuficientes |
| Taberna Delicatessen | S2 | 10 | 0 | 30 | 31,4% | 0,30 | 3 | Dados insuficientes |

Os casos são referências metodológicas, não leads atuais nem autorização para abordagem.

## 9. Regra operacional final

O agente deve preferir qualidade e rastreabilidade a volume. Se não conseguir comprovar um dado, deve declarar a limitação e manter a pendência. Nunca converter ausência de informação em afirmação positiva ou negativa sem cumprir o protocolo correspondente.
