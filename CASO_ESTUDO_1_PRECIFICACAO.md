# Caso de Estudo 1: Sistema de Precificação E-commerce

## 📊 Contexto
**Empresa:** Fox Pet Shop LTDA EPP  
**Período:** 2025  
**Volume:** 6.000 pedidos/mês  
**Desafio:** Vendas com margem negativa | Falta de controle de precificação

---

## 🎯 Desafio Identificado

A Fox Pet Shop operava com:
- ❌ Precificação manual e inconsistente
- ❌ Produtos vendidos com margem negativa
- ❌ Falta de visibilidade de custos por marketplace
- ❌ Dificuldade em competir preços

**Impacto:** Prejuízo direto nas operações de e-commerce

---

## 💡 Solução Desenvolvida

### Fase 1: Análise
- Mapeou taxas de cada marketplace (Mercado Livre 11%, Amazon 15%, Shopee 10%, TikTok 5%, B2Brazil 8%)
- Identificou inconsistências de precificação
- Calculou custo real por canal de venda

### Fase 2: Desenvolvimento
Contribuí na implementação de um **sistema de precificação híbrido** (automações low-code, SQL e scripts auxiliares) que:

```python
# Fórmula utilizada:
Preço Venda = Custo / (1 - Taxa Total - Margem Desejada)

# Exemplo prático:
- Custo: R$ 50
- Margem: 30%
- TikTok Shop (5% + 2%): R$ 79,37 ✓ LUCRO
- Amazon (15% + 2.9%): R$ 95,97 ✓ LUCRO
```

Além disso, implementei um **avisador automático de margem** que monitorava vendas em tempo real e gerava alertas quando a margem estava abaixo dos limites definidos (com flag de atenção em vendas detectadas abaixo de 5%, sendo a margem alvo mínima definida em 6%). A arquitetura do avisador incluiu:

- Checagem de ordens e cálculo de margem via consultas SQL em Supabase (Webhooks / Triggers / Scheduled Functions)
- Integração com APIs dos marketplaces (Mercado Livre, Shopee, Nuvem Shop) e ERP (Tiny) para obter custo, taxas e vendas
- Envio automático de e-mail ao time responsável por precificação (ex.: SendGrid) com SKU, preço praticado, margem calculada e link para revisão
- Fluxo de auditoria: registro dos alertas no Supabase para análise e follow-up

**Features principais:**
- ✓ Cálculo automático por marketplace
- ✓ Monitoramento e alertas de margem (thresholds configuráveis)
- ✓ Notificações por e-mail para time de precificação
- ✓ Comparação de rentabilidade e dashboard para revisão rápida
- ✓ Simulações de cenários e auditoria de histórico de alertas

### Fase 3: Implementação
- Integração com processos de precificação
- Treinamento da equipe
- Aplicação em 6.000 SKUs

### Fase 4: Otimização
- Análise de dados de vendas
- Ajustes conforme demanda
- Validação de margens

---

## 📈 Resultados Alcançados

| Métrica | Antes | Depois | Melhoria |
|---------|-------|--------|----------|
| % Vendas com margem negativa | 18% | 0% | 📉 -18% |
| Tempo precificação/produto | 5 min | 30 seg | ⚡ 10x mais rápido |
| Margem média | 12% | 30% | 📈 +150% |
| Erro de precificação | 22% | <1% | 🎯 99% acurácia |
| Confiança em rentabilidade | Baixa | Alta | ✓ 100% |

---

## 🛠️ Tecnologias Utilizadas

- **Ferramentas:** Supabase (Postgres + Functions), SQL, automações low-code (Zapier/Make), scripts auxiliares (Python básico)
- **Integrações de dados:** APIs Mercado Livre, Shopee, Nuvem Shop e ERP Tiny (sincronização de preços, custos e ordens)
- **Notificações:** Envio de e-mail automático (ex.: SendGrid) e registro de alertas em Supabase
- **Dados:** Análise de 6.000 transações/mês

---

## 🎓 Aprendizados & Impacto Comercial

### Competências Desenvolvidas
- Análise de dados de e-commerce
- Modelagem matemática de preços
- Otimização de margens
- Automação de processos

### Impacto nos Negócios
✅ **Eliminação de prejuízos** - 0% de margem negativa  
✅ **Aumento de rentabilidade** - +150% de margem  
✅ **Eficiência operacional** - 10x mais rápido  
✅ **Escabilidade** - Sistema pronto para 50.000+ SKUs

### Para Empresas Remotas
Este projeto demonstra:
- 💼 Capacidade de **resolver problemas reais** com dados
- 🔧 Habilidade de **automação de processos**
- 📊 Pensamento **analítico** em e-commerce
- 🚀 Foco em **resultados mensuráveis**

---

## 💻 Código Disponível

📎 **GitHub:** [github.com/harleybonfatti/marketplace-pricing-calculator](https://github.com)  
🔗 **Demo ao vivo:** [Executável no seu PC]

---

## 📞 Impacto Potencial para sua Empresa

Se você enfrenta:
- Dúvida sobre precificação correta
- Prejuízo em vendas online
- Inconsistência entre canais
- Impossibilidade de garantir margem

**Esta solução:**
✓ Calcula preço ótimo automaticamente  
✓ Garante margem desejada  
✓ Funciona em todos os marketplaces  
✓ Economiza 90% do tempo de precificação

---

## 🎯 Métricas de Sucesso (KPIs)

```
📊 Antes vs Depois
├─ Vendas com prejuízo: 18% → 0%
├─ Tempo/SKU: 5min → 30seg  
├─ Margem: 12% → 30%
└─ Acurácia: 78% → 99%
```

---

**Harley Bonfatti** | Assistente de E-commerce  
Atuação com automações low-code, SQL e apoio em scripts
