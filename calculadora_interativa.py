#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

# Script que abre a calculadora em modo interativo
def main():
    print("\n" + "="*80)
    print("CALCULADORA DE PRECOS - MARKETPLACES")
    print("="*80 + "\n")
    
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    from marketplace_calculator import MarketplaceCalculator
    
    calc = MarketplaceCalculator()
    
    while True:
        print("\n[MENU]")
        print("1. Comparar todos os marketplaces")
        print("2. Calcular preco para um marketplace especifico")
        print("3. Ver tabela de simulacoes")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opcao (1-4): ").strip()
        
        if opcao == "1":
            try:
                custo = float(input("\nDigite o preco de custo (R$): "))
                margem = float(input("Digite a margem desejada (%) [padrao 30]: ") or "30") / 100
                calc.comparar_marketplaces(custo, margem)
            except ValueError:
                print("Erro: Digite um valor numerico valido!")
        
        elif opcao == "2":
            try:
                print("\nMarketplaces disponiveis:")
                for i, chave in enumerate(calc.MARKETPLACES.keys(), 1):
                    print(f"  {i}. {calc.MARKETPLACES[chave]['nome']}")
                
                mp_idx = int(input("\nEscolha o marketplace (numero): ")) - 1
                mp_lista = list(calc.MARKETPLACES.keys())
                
                if 0 <= mp_idx < len(mp_lista):
                    mp = mp_lista[mp_idx]
                    custo = float(input("Digite o preco de custo (R$): "))
                    margem = float(input("Digite a margem desejada (%) [padrao 30]: ") or "30") / 100
                    
                    resultado = calc.calcular_preco_final(custo, margem, mp)
                    dados = resultado[mp]
                    
                    print(f"\n{dados['marketplace']}")
                    print(f"Preco de venda: R$ {dados['preco_venda']:.2f}")
                    print(f"Taxas totais: R$ {dados['total_taxas']:.2f}")
                    print(f"Lucro liquido: R$ {dados['lucro_liquido']:.2f}")
                    print(f"Margem real: {dados['margem_real']:.2f}%")
                else:
                    print("Opcao invalida!")
            except ValueError:
                print("Erro: Digite um valor numerico valido!")
        
        elif opcao == "3":
            try:
                custo = float(input("\nDigite o preco de custo (R$): "))
                margem = float(input("Digite a margem desejada (%) [padrao 30]: ") or "30") / 100
                calc.tabela_precos(custo, margem)
            except ValueError:
                print("Erro: Digite um valor numerico valido!")
        
        elif opcao == "4":
            print("\nSaindo... Ate logo!")
            break
        
        else:
            print("Opcao invalida! Digite 1, 2, 3 ou 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido. Ate logo!")
    except Exception as e:
        print(f"\nErro: {e}")
        input("\nPressione ENTER para sair...")
