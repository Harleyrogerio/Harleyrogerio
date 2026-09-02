# Case Study 1: E-commerce Pricing System

## Context
**Company:** Fox Pet Shop LTDA EPP  
**Period:** 2025  
**Volume:** 6,000 orders/month  
**Challenge:** Sales with negative or very low margins; lack of pricing control across marketplaces

---

## Problem Identified

Fox Pet Shop faced:
- Manual and inconsistent pricing
- Products sold below acceptable contribution margin
- No centralized visibility of costs per marketplace
- Difficulty competing on price while protecting margin

**Impact:** Direct revenue leakage and margin erosion

---

## Solution Delivered

I contributed to a hybrid pricing system (low-code automations, SQL, and supporting scripts) that automated price calculation per marketplace using the formula:

```
Sale Price = Cost / (1 - Total Fees - Desired Margin)
```

In addition, I helped implement a real-time margin alert system with these components:

- Margin checks and calculations stored in Supabase (Postgres) using webhooks/triggers and scheduled functions
- Integrations with marketplace APIs (Mercado Livre, Shopee, Nuvem Shop) and ERP (Tiny) to fetch costs, fees, and orders
- Automated email notifications (e.g., SendGrid) to the pricing team when a sale or listing is detected below the threshold (minimum margin target: 6%; alert threshold set at 5%)
- Alert audit logs stored in Supabase for review and follow-up

### Key features
- Automated price calculation per marketplace
- Real-time margin monitoring with configurable thresholds
- Email notifications with SKU, sold price, calculated margin, and review link
- Dashboard for quick triage and historical alert analysis
- Scenario simulations for pricing decisions

---

## Technologies Used

- Supabase (Postgres + Functions) for data, triggers and alert logs
- SQL for margin calculations and reporting
- Marketplace APIs: Mercado Livre, Shopee, Nuvem Shop
- ERP integration: Tiny
- Notifications: SendGrid (email) and Zapier/Make for orchestration
- Supporting Python scripts (basic) for auxiliary ETL and API calls

---

## Results

- Sales with negative margin: 18% → 0% (full elimination of margin-negative sales)
- Average margin: 12% → 30% (+150%)
- Time per SKU pricing reduced by ~80%
- Devolutions reduced and operational efficiency increased

---

## Skills Demonstrated
- Data analysis and SQL-based pricing logic
- Low-code/no-code automation and orchestration
- API integrations with marketplaces and ERP
- Building monitoring and alerting for commercial KPIs

---

**Harley Bonfatti** | E-commerce Assistant
Contributed using low-code automations, SQL, Supabase and supporting scripts.
