#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Preços - Marketplaces Brasileiros
Calcula o preço final com todas as taxas e comissões
"""

class MarketplaceCalculator:
    """Calculadora de preços com taxas específicas de cada marketplace"""
    
    MARKETPLACES = {
        'mercado_livre': {
            'nome': 'Mercado Livre',
            'comissao': 0.11,  # 11%
            'taxa_pagamento': 0.029,  # 2.9%
            'taxa_frete': 0,
            'descricao': 'Comissão: 11% + Taxa de pagamento: 2.9%'
        },
        'amazon': {
            'nome': 'Amazon',
            'comissao': 0.15,  # 15%
            'taxa_pagamento': 0.029,  # 2.9%
            'taxa_frete': 0,
            'descricao': 'Comissão: 15% + Taxa de pagamento: 2.9% (1º ano sem mensalidade)'
        },
        'shopee': {
            'nome': 'Shopee',
            'comissao': 0.10,  # 10%
            'taxa_pagamento': 0.025,  # 2.5%
            'taxa_frete': 0,
            'descricao': 'Comissão: 10% + Taxa de pagamento: 2.5%'
        },
        'tiktok_shop': {
            'nome': 'TikTok Shop',
            'comissao': 0.05,  # 5%
            'taxa_pagamento': 0.02,  # 2%
            'taxa_frete': 0,
            'descricao': 'Comissão: 5% + Taxa de pagamento: 2%'
        },
        'b2brazil': {
            'nome': 'B2Brazil',
            'comissao': 0.08,  # 8%
            'taxa_pagamento': 0.015,  # 1.5%
            'taxa_frete': 0,
            'descricao': 'Comissão: 8% + Taxa de pagamento: 1.5%'
        }
    }
    
    def __init__(self):
        self.resultados = []
    
    def calcular_preco_final(self, preco_custo, margem_lucro=0.30, marketplace=None):
        """
        Calcula o preço final com margem de lucro e taxas
        
        Args:
            preco_custo: Preço de custo do produto
            margem_lucro: Margem de lucro desejada (padrão 30%)
            marketplace: Nome do marketplace (None = calcula todos)
        
        Returns:
            Dict com os preços calculados
        """
        if marketplace and marketplace not in self.MARKETPLACES:
            return {'erro': f'Marketplace {marketplace} não encontrado'}
        
        mercados = {marketplace: self.MARKETPLACES[marketplace]} if marketplace else self.MARKETPLACES
        resultados = {}
        
        for chave, dados in mercados.items():
            # Cálculo: Preço de venda necessário para manter margem após taxas
            # Preço venda = Custo / (1 - taxa_total - margem)
            taxa_total = dados['comissao'] + dados['taxa_pagamento']
            
            # Preço com margem
            preco_venda = preco_custo / (1 - taxa_total - margem_lucro)
            
            # Valores de taxas
            valor_comissao = preco_venda * dados['comissao']
            valor_taxa_pag = preco_venda * dados['taxa_pagamento']
            valor_total_taxas = valor_comissao + valor_taxa_pag
            
            # Lucro real
            lucro = preco_venda - preco_custo - valor_total_taxas
            
            resultados[chave] = {
                'marketplace': dados['nome'],
                'preco_custo': round(preco_custo, 2),
                'preco_venda': round(preco_venda, 2),
                'comissao': round(valor_comissao, 2),
                'taxa_pagamento': round(valor_taxa_pag, 2),
                'total_taxas': round(valor_total_taxas, 2),
                'lucro_liquido': round(lucro, 2),
                'margem_real': round((lucro / preco_venda) * 100, 2),
                'descricao': dados['descricao']
            }
        
        return resultados
    
    def comparar_marketplaces(self, preco_custo, margem_lucro=0.30):
        """Compara preços e lucros entre todos os marketplaces"""
        resultados = self.calcular_preco_final(preco_custo, margem_lucro)
        
        print(f"\n{'='*100}")
        print(f"COMPARAÇÃO DE PREÇOS - Custo: R$ {preco_custo:.2f} | Margem desejada: {margem_lucro*100:.0f}%")
        print(f"{'='*100}\n")
        
        # Ordena por preço de venda (menor para maior)
        ordenado = sorted(resultados.items(), key=lambda x: x[1]['preco_venda'])
        
        for chave, dados in ordenado:
            print(f"\n[{dados['marketplace'].upper()}]")
            print(f"   Descricao: {dados['descricao']}")
            print(f"   Preco de Venda:    R$ {dados['preco_venda']:>8.2f}")
            print(f"   |- Comissao:       R$ {dados['comissao']:>8.2f} ({self.MARKETPLACES[chave]['comissao']*100:.1f}%)")
            print(f"   |- Taxa Pagamento: R$ {dados['taxa_pagamento']:>8.2f} ({self.MARKETPLACES[chave]['taxa_pagamento']*100:.1f}%)")
            print(f"   |- Total Taxas:    R$ {dados['total_taxas']:>8.2f}")
            print(f"   `- Lucro Liquido:  R$ {dados['lucro_liquido']:>8.2f} ({dados['margem_real']:.1f}%)")
    
    def tabela_precos(self, preco_custo, margem_lucro=0.30):
        """Exibe tabela formatada com todos os marketplaces"""
        resultados = self.calcular_preco_final(preco_custo, margem_lucro)
        
        print(f"\n{'MARKETPLACE':<15} {'VENDA':<12} {'TAXAS':<12} {'LUCRO':<12} {'MARGEM':<10}")
        print(f"{'-'*65}")
        
        for chave, dados in sorted(resultados.items(), key=lambda x: x[1]['preco_venda']):
            print(f"{dados['marketplace']:<15} "
                  f"R${dados['preco_venda']:>9.2f}  "
                  f"R${dados['total_taxas']:>9.2f}  "
                  f"R${dados['lucro_liquido']:>9.2f}  "
                  f"{dados['margem_real']:>7.1f}%")
        
        print(f"{'-'*65}\n")
    
    def simular_diferentes_custos(self, custos, margem_lucro=0.30):
        """Simula preços para diferentes custos"""
        print(f"\n{'='*90}")
        print(f"SIMULAÇÃO PARA DIFERENTES CUSTOS (Margem: {margem_lucro*100:.0f}%)")
        print(f"{'='*90}\n")
        
        for custo in custos:
            self.tabela_precos(custo, margem_lucro)


def main():
    calc = MarketplaceCalculator()
    
    # Exemplo 1: Produto com custo de R$ 50
    print("\n" + "="*100)
    print("EXEMPLO 1: Calculando preço para produto com custo R$ 50")
    print("="*100)
    calc.comparar_marketplaces(50, margem_lucro=0.30)
    
    # Exemplo 2: Produto com custo de R$ 100
    print("\n" + "="*100)
    print("EXEMPLO 2: Calculando preço para produto com custo R$ 100")
    print("="*100)
    calc.comparar_marketplaces(100, margem_lucro=0.30)
    
    # Exemplo 3: Simulação com diferentes custos
    custos = [10, 25, 50, 100, 500]
    calc.simular_diferentes_custos(custos, margem_lucro=0.30)
    
    # Exemplo 4: Comparação apenas Mercado Livre
    print("\n" + "="*100)
    print("EXEMPLO 4: Detalhamento Mercado Livre - Custo R$ 50")
    print("="*100)
    resultado = calc.calcular_preco_final(50, 0.30, 'mercado_livre')
    dados = resultado['mercado_livre']
    print(f"\nCusto do produto:      R$ {dados['preco_custo']:.2f}")
    print(f"Preço de venda:        R$ {dados['preco_venda']:.2f}")
    print(f"Comissão (11%):        R$ {dados['comissao']:.2f}")
    print(f"Taxa de pagamento:     R$ {dados['taxa_pagamento']:.2f}")
    print(f"Total de taxas:        R$ {dados['total_taxas']:.2f}")
    print(f"Lucro líquido:         R$ {dados['lucro_liquido']:.2f}")
    print(f"Margem real:           {dados['margem_real']:.2f}%")


if __name__ == "__main__":
    main()
