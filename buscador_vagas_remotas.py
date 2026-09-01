#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Busca Automática de Vagas Remotas
Busca diariamente em principais sites e envia resumo por email
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json

class VagasRemotasScraperCV:
    """Scraper de vagas remotas para Customer Success"""
    
    def __init__(self):
        self.vagas = []
        self.hoje = datetime.now().strftime("%Y-%m-%d %H:%M")
        
    def buscar_we_work_remotely(self):
        """Busca vagas em We Work Remotely"""
        print("🔍 Buscando em We Work Remotely...")
        
        # URL da categoria Customer Success
        url = "https://weworkremotely.com/categories/customer-support-success"
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Encontra cards de vagas (estrutura pode variar)
            vagas_html = soup.find_all('div', class_='job-listing')
            
            for vaga in vagas_html[:5]:  # Top 5
                titulo = vaga.find('h2')
                empresa = vaga.find('span', class_='company')
                link = vaga.find('a', href=True)
                
                if titulo and empresa and link:
                    self.vagas.append({
                        'titulo': titulo.text.strip(),
                        'empresa': empresa.text.strip(),
                        'link': link['href'],
                        'site': 'We Work Remotely',
                        'data': self.hoje
                    })
            
            print(f"   ✓ Encontradas {len([v for v in self.vagas if v['site'] == 'We Work Remotely'])} vagas")
        
        except Exception as e:
            print(f"   ✗ Erro: {e}")
    
    def buscar_remote_co(self):
        """Busca vagas em Remote.co"""
        print("🔍 Buscando em Remote.co...")
        
        url = "https://remote.co/remote-jobs/customer-success"
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            vagas_html = soup.find_all('div', class_='job-item')
            
            for vaga in vagas_html[:5]:
                titulo = vaga.find('h2', class_='job-title')
                empresa = vaga.find('span', class_='company-name')
                link = vaga.find('a', href=True)
                
                if titulo and empresa and link:
                    self.vagas.append({
                        'titulo': titulo.text.strip(),
                        'empresa': empresa.text.strip(),
                        'link': link['href'],
                        'site': 'Remote.co',
                        'data': self.hoje
                    })
            
            print(f"   ✓ Encontradas {len([v for v in self.vagas if v['site'] == 'Remote.co'])} vagas")
        
        except Exception as e:
            print(f"   ✗ Erro: {e}")
    
    def buscar_remoteok(self):
        """Busca vagas em RemoteOK"""
        print("🔍 Buscando em RemoteOK...")
        
        url = "https://remoteok.io/remote-customer-support-jobs"
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            vagas_html = soup.find_all('tr', {'class': 'job'})
            
            for vaga in vagas_html[:5]:
                titulo = vaga.find('h2')
                empresa = vaga.find('h3')
                link = vaga.find('a', href=True)
                
                if titulo and empresa and link:
                    self.vagas.append({
                        'titulo': titulo.text.strip(),
                        'empresa': empresa.text.strip(),
                        'link': link['href'],
                        'site': 'RemoteOK',
                        'data': self.hoje
                    })
            
            print(f"   ✓ Encontradas {len([v for v in self.vagas if v['site'] == 'RemoteOK'])} vagas")
        
        except Exception as e:
            print(f"   ✗ Erro: {e}")
    
    def buscar_linkedin(self):
        """Busca vagas no LinkedIn (simulado)"""
        print("🔍 Buscando no LinkedIn...")
        print("   ℹ️  Para LinkedIn, use filtros:")
        print("      - Título: 'Customer Success Manager'")
        print("      - Localização: 'Remoto'")
        print("      - Novo: 'Último mês'")
        print("      - URL: linkedin.com/jobs/search/?keywords=Customer Success Manager&location=Remoto")
    
    def gerar_relatorio(self):
        """Gera relatório formatado"""
        print("\n" + "="*80)
        print(f"📊 RELATORIO DE VAGAS REMOTAS - {self.hoje}")
        print("="*80)
        print(f"\nTotal de vagas encontradas: {len(self.vagas)}\n")
        
        # Agrupa por site
        por_site = {}
        for vaga in self.vagas:
            site = vaga['site']
            if site not in por_site:
                por_site[site] = []
            por_site[site].append(vaga)
        
        for site, vagas_site in por_site.items():
            print(f"\n🏢 {site.upper()} ({len(vagas_site)} vagas)")
            print("-" * 80)
            
            for i, vaga in enumerate(vagas_site, 1):
                print(f"\n{i}. {vaga['titulo']}")
                print(f"   Empresa: {vaga['empresa']}")
                print(f"   Link: {vaga['link']}")
        
        print("\n" + "="*80)
    
    def salvar_json(self, filename="vagas_encontradas.json"):
        """Salva vagas em JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.vagas, f, ensure_ascii=False, indent=2)
        print(f"\n✓ Vagas salvas em: {filename}")
    
    def salvar_csv(self, filename="vagas_encontradas.csv"):
        """Salva vagas em CSV para Excel"""
        import csv
        
        if not self.vagas:
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['titulo', 'empresa', 'site', 'link', 'data'])
            writer.writeheader()
            writer.writerows(self.vagas)
        
        print(f"✓ Vagas salvas em: {filename} (abrir no Excel)")
    
    def filtrar_relevantes(self, keywords=None):
        """Filtra vagas por palavras-chave"""
        if keywords is None:
            keywords = ['customer success', 'operations', 'automation', 'remote', 'csr', 'account']
        
        relevantes = []
        for vaga in self.vagas:
            titulo_lower = vaga['titulo'].lower()
            if any(keyword in titulo_lower for keyword in keywords):
                relevantes.append(vaga)
        
        return relevantes
    
    def executar(self):
        """Executa todas as buscas"""
        print("\n" + "="*80)
        print("🚀 BUSCADOR AUTOMÁTICO DE VAGAS REMOTAS")
        print("="*80 + "\n")
        
        self.buscar_we_work_remotely()
        self.buscar_remote_co()
        self.buscar_remoteok()
        self.buscar_linkedin()
        
        self.gerar_relatorio()
        self.salvar_json()
        self.salvar_csv()
        
        # Filtrar por relevância
        relevantes = self.filtrar_relevantes()
        print(f"\n🎯 Vagas relevantes para você: {len(relevantes)}")
        
        return self.vagas


def main():
    scraper = VagasRemotasScraperCV()
    vagas = scraper.executar()
    
    print("\n✅ Busca concluída!")
    print("📁 Arquivos gerados:")
    print("   - vagas_encontradas.json (para análise)")
    print("   - vagas_encontradas.csv (abrir no Excel)")
    print("\n💡 Dica: Abra o CSV no Excel e crie filtros personalizados")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBusca interrompida.")
    except Exception as e:
        print(f"\n✗ Erro: {e}")
        print("Dica: Instale requisitos com: pip install requests beautifulsoup4")
