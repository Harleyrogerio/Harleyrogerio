# 💻 Como Usar os Projetos

## 1️⃣ Calculadora de Preços por Marketplace

### O Que Faz
Calcula automaticamente o preço de venda garantindo sua margem em cada marketplace.

### Como Instalar

**Windows:**
```bash
# 1. Abra Power Shell ou CMD
# 2. Navegue até a pasta do projeto
cd seu_caminho_aqui

# 3. Instale Python (se não tiver)
# Baixe em: https://www.python.org/downloads/

# 4. Instale as dependências
pip install --upgrade pip

# 5. Pronto! Não precisa de mais nada
```

### Como Usar

**Opção 1: Executar pelo Atalho (Mais Fácil)**
```
Procure no Desktop: "Calculadora.lnk" ou "Calculadora Preços.lnk"
Clique 2x
Menu aparece automaticamente
```

**Opção 2: Pela Linha de Comando**
```bash
cd seu_caminho
python calculadora_interativa.py
```

**Opção 3: Arquivo Python Direto**
```bash
# Para teste mais técnico
python marketplace_calculator.py
```

### Como Usar (Interface)

```
====================================
    CALCULADORA DE PREÇOS
   Multiple Marketplace v1.0
====================================

[1] Shopee
[2] TikTok Shop
[3] B2Brazil
[4] Mercado Livre
[5] Amazon (1º ano sem taxa)
[6] Sair

Digite sua escolha (1-6): 1

========== SHOPEE ==========
Custo do produto (R$): 100
Margem desejada (%): 30

Resultado:
├─ Custo: R$ 100,00
├─ Taxa Shopee: 12,5%
├─ Margem desejada: 30%
└─ PREÇO FINAL: R$ 181,82

Você vai ganhar: R$ 30,00 por venda
```

### Exemplo Prático

**Cenário:**
- Você compra um produto por R$ 100
- Quer ganhar 30% de margem
- Quer vender na Shopee (que cobra 12.5%)

**Sem Sistema:**
❌ Coloca R$ 150 (pensando em 50% markup)
❌ Esqueceu que Shopee cobra 12.5%
❌ Recebe: R$ 131,25
❌ Lucro real: R$ 31,25 (apenas 31%, não 50%)

**Com Sistema:**
✅ Sistema calcula: R$ 181,82
✅ Shopee cobra 12.5%: -R$ 22,73
✅ Você recebe: R$ 159,09
✅ Lucro real: R$ 59,09 (exatamente 30%!)

### Marketplaces Suportados

| Marketplace | Taxa | Descrição |
|------------|------|-----------|
| Shopee | 12.5% | +2.5% gateway |
| TikTok Shop | 7% | Melhor custo-benefício |
| B2Brazil | 9.5% | +1.5% gateway |
| Mercado Livre | 13.9% | +2.9% gateway |
| Amazon | 17.9% | Sem mensalidade no 1º ano |

### Arquivos Relacionados
- `marketplace_calculator.py` - Versão programável (para desenvolvedores)
- `calculadora_interativa.py` - Versão amigável (para todos)

---

## 2️⃣ Buscador Automático de Vagas Remotas

### O Que Faz
Busca automaticamente vagas remotas em 4 sites diferentes e salva em um CSV (Excel) para você revisar.

### Como Instalar

```bash
# 1. Abra Power Shell ou CMD
cd seu_caminho

# 2. Instale as dependências
pip install beautifulsoup4 requests

# 3. Pronto!
```

### Como Usar

```bash
python buscador_vagas_remotas.py
```

### O Que Esperar

```
Iniciando busca...

[1/4] Buscando em We Work Remotely...
  └─ Encontrou 23 vagas
  
[2/4] Buscando em Remote.co...
  └─ Encontrou 18 vagas
  
[3/4] Buscando em RemoteOK...
  └─ Encontrou 45 vagas
  
[4/4] Buscando em LinkedIn...
  └─ Encontrou 67 vagas

Total: 153 vagas encontradas!

Salvando em: vagas_remotas.csv
```

### Abrindo o Resultado

1. Procure por: `vagas_remotas.csv`
2. Clique com botão direito → Abrir com Excel
3. Vê todas as vagas, link, empresa, cargo

### Exemplo de Output

| Cargo | Empresa | Link | Data |
|-------|---------|------|------|
| Customer Success Manager | Stripe | https://... | 2026-09-01 |
| Operations Lead | Notion | https://... | 2026-08-31 |
| CS Manager | Intercom | https://... | 2026-08-30 |

### Como Usar Resultado

1. **Abra o CSV** (Excel)
2. **Procure por palavras-chave:** "Customer Success", "Operations", "Manager"
3. **Filtre por empresa** que conhece
4. **Copie o link** → acessa a vaga
5. **Envia seu CV** ou conecta no LinkedIn

### Dica Pro

```bash
# Rodar toda semana (segunda-feira)
# Cria um arquivo com data: vagas_remotas_2026-09-01.csv

python buscador_vagas_remotas.py

# Depois de usar:
# Copie as vagas interessantes para uma planilha de controle
```

---

## 3️⃣ Plano de Carreira 8 Semanas

### O Que É
Guia completo passo a passo para conseguir trabalho remoto em Customer Success.

### Como Usar

**Abra:** `README_PLANO_CARREIRA.md`

**Semana 1:**
- [ ] Otimize LinkedIn
- [ ] Crie portfólio online
- [ ] Prepare currículo ATS
- [ ] Pesquise 15 empresas
- [ ] Encontre 15 recrutadores

**Semana 2-3:**
- [ ] Adicione 15 empresas (total 30)
- [ ] Adicione 15 recrutadores (total 30)
- [ ] Envie 10 emails (Template 5)
- [ ] Aja em informational interviews
- [ ] Participe de comunidades

**Semana 4+:**
- [ ] Cold emails (5/semana, Template 1)
- [ ] Aplicações (3/semana, Template 3)
- [ ] LinkedIn DMs (5/semana, Template 4)
- [ ] Rode buscador de vagas
- [ ] Prepare para entrevistas

---

## 4️⃣ Templates de Email

### O Que São
5 templates prontos para copiar/colar e personalizar.

### Como Usar

**Abra:** `EMAIL_TEMPLATE_RECRUTADORES.md`

### Qual Template Para Que?

**Template 1: Cold Email**
- Quando: Empresa que não conhece
- Usa para: Primeiro contato
- Chancela: 5-10%
- Frequência: 1x por semana (máximo)

**Template 2: Personalized**
- Quando: Você se conectou no LinkedIn
- Usa para: Seguir up depois de conectar
- Chancela: 15-20%
- Frequência: 2x por semana

**Template 3: Follow-up**
- Quando: Aplicou em vaga aberta
- Usa para: Reforçar interesse
- Chancela: 20-30%
- Frequência: Após 5 dias da aplicação

**Template 4: LinkedIn Message**
- Quando: Mensagem privada no LinkedIn
- Usa para: Contato mais direto
- Chancela: 10-15%
- Frequência: 3x por semana

**Template 5: Informational Interview**
- Quando: Pedir conversa rápida
- Usa para: Warm up antes de aplicar
- Chancela: 25-35%
- Frequência: Semanas 1-3 (depois aplica)

### Dica: Personalização

```
❌ NÃO FAÇA (Genérico)
Assunto: Interesse em Customer Success Manager

Olá,

Tenho interesse em trabalhar na sua empresa...

---

✅ FAÇA (Personalizado)
Assunto: 82% revenue growth em marketplace - sua próxima oportunidade

Olá João,

Vi que você lidera o time de CS na Empresa X. 
Implementei +82% de receita em 6 meses no marketplace.
Seria legal trocar uma ideia?

- Harley
```

**Regra:** Sempre cite:
- Nome da pessoa (procure no LinkedIn)
- Nome da empresa (não genérico)
- Um número do seu trabalho (+82%, -67%, etc)

---

## 5️⃣ Arquivos de Estudo

### Caso 1: Precificação
Abra: `CASO_ESTUDO_1_PRECIFICACAO.md`
- Ideal para: Tech, SaaS, empresas com margem
- Demonstra: Python, análise, lógica

### Caso 2: CRM Clínicas
Abra: `CASO_ESTUDO_2_CRM_CLINICAS.md`
- Ideal para: Operations, Automação, CS Manager
- Demonstra: Supabase, webhooks, automação

### Caso 3: Marketplace ⭐
Abra: `CASO_ESTUDO_3_ECOMMERCE.md`
- Ideal para: Qualquer vaga (+82% sempre impressiona)
- Demonstra: Multi-skill, impacto, escalabilidade

### Qual Compartilhar?

```
Recrutador procura:        Compartilhe:
"Automação"      →         Caso 2 (CRM)
"Growth"         →         Caso 3 (Marketplace)
"Analytics"      →         Caso 1 (Precificação)
"Operações"      →         Caso 3 (Marketplace)
"Tech"           →         Caso 2 (CRM) + Código
"Incerteza"      →         Caso 3 (Marketplace - +82%)
```

---

## 6️⃣ Métricas & Visualização

### O Que É
Dashboard visual mostrando todos seus resultados.

### Como Usar

Abra: `METRICAS.md`

Compartilhe em:
- LinkedIn (coloca link no post)
- Email para recrutador
- Portfolio online
- Apresentação em entrevista

---

## 🚀 Fluxo Completo Recomendado

### Semana 1-2 (Preparação)
```
1. Leia: INDICE_COMPLETO.md
2. Leia: README_PLANO_CARREIRA.md
3. Abra: METRICAS.md
4. Otimize: LinkedIn
5. Crie: Portfólio online
```

### Semana 3-4 (Outreach)
```
1. Rode: buscador_vagas_remotas.py (segunda)
2. Envie: 10 emails (Template 5)
3. Agende: Informational interviews
4. Estude: seus casos de estudo
```

### Semana 5+ (Aplicações)
```
1. Rode: buscador_vagas_remotas.py (toda semana)
2. Aplique: 3 vagas/semana (Template 3)
3. Cold email: 5/semana (Template 1)
4. LinkedIn DM: 5/semana (Template 4)
5. Prepara: para entrevistas
```

---

## ❓ FAQ

**P: Preciso mudar algo nos templates?**  
R: SIM! Mude nome, empresa, números. Genérico não funciona.

**P: Buscador encontra muitas vagas?**  
R: Depende do site. Em média 100-150/semana. Depois filtra o que te interessa.

**P: Debo usar tudo ou escolher?**  
R: Comece com: Calculadora (básico) + Plano carreira (estratégia) + Templates (ação)

**P: Qual template mais eficaz?**  
R: Template 5 (Informational) é melhor taxa de resposta (25-35%).

**P: Posso modificar o código?**  
R: Claro! É seu! Adapte para suas necessidades.

---

## 💡 Dicas Finais

1. **Executar > Perfeição**  
   Comece AGORA. 80% pronto bate 100% nunca.

2. **Personalização é Tudo**  
   Copy/paste genérico = taxa 0%. Personalizado = taxa 20%+.

3. **Consistência mata perfeccionismo**  
   5 emails/semana durante 8 semanas > 50 emails em 1 semana.

4. **Numeros impressionam**  
   Sempre cite: +82%, -67%, +40%, +150%. Números abrem portas.

5. **Rode semanalmente**  
   Buscador de vagas todo segunda.  
   Emails toda terça/quarta/quinta.  
   Follow-ups toda sexta.

---

**Você tem tudo. Agora é executar.** 💪

*Última atualização: Setembro 2026*
