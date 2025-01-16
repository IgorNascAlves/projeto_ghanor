# Projeto: Monitoramento de Financiamento Coletivo - Jovem Nerd

## Autor
**Igor Nascimento Alves**

## Descrição
Este projeto foi desenvolvido com o objetivo de monitorar e visualizar o progresso de campanhas de financiamento coletivo, como o do Jovem Nerd. Ele utiliza uma arquitetura robusta e ferramentas modernas para extrair, transformar e carregar dados de forma automatizada, permitindo análises avançadas e visualizações intuitivas. Este projeto também demonstra as competências essenciais de um engenheiro de dados, como orquestração de pipelines, criação de data lakes e utilização de ferramentas analíticas.

## Arquitetura
![Arquitetura do Projeto](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/8c07aecb-718d-4c72-a941-62c59740c2a7)

A arquitetura do projeto é dividida em três áreas principais:

1. **DataEng:**
   - **API - LuizaLabs:** Fonte de dados da campanha de financiamento coletivo.
   - **Airflow:** Orquestração de pipelines para extração e carregamento dos dados.
   - **Data Lake:** Repositório central para armazenamento dos dados em diferentes camadas (bruto, processado).

2. **DataScience:**
   - **Notebook:** Ferramenta para análise exploratória de dados e criação de modelos preditivos baseados nos dados armazenados no data lake.

3. **DataAnalytics:**
   - **Power BI:** Criação de dashboards interativos para visualização do progresso da campanha e insights derivados dos dados.

## Tecnologias Utilizadas
- **Python:** Para desenvolvimento dos scripts de coleta e processamento de dados.
- **Apache Airflow:** Para orquestração dos pipelines de dados.
- **Flask:** Framework para desenvolvimento da aplicação web inicial.
- **Pandas:** Para manipulação e análise de dados.
- **Power BI:** Para criação de dashboards analíticos.
- **Data Lake:** Implementado localmente para armazenamento de dados estruturados e não estruturados.

## Funcionalidades
- **Extração de Dados:** Coleta de informações da API do financiamento coletivo.
- **Armazenamento em Data Lake:** Dados salvos em camadas (bronze, silver) para garantir histórico e integridade.
- **Pipeline Automatizado:** Orquestração diária utilizando Apache Airflow.
- **Visualizações Avançadas:** Dashboards interativos no Power BI para análise do desempenho da campanha.
- **Histórico de Arrecadação:** Rastreio do progresso da campanha em tempo real.

## Análise Power BI

![Análise Power BI - Visão Geral](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/f9018c10-f129-43eb-903e-2d7378c6d06f)

![Análise Power BI - Detalhes](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/c9a60fbe-f1ec-4f14-a9f3-82b1392ee812)

## Aplicação

![Aplicação - Dashboard Inicial](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/2a95c9bf-0045-4c56-967a-65f6ce1ef078)

## Comparação de Campanhas
Explore os dados e análises comparativas diretamente na página abaixo:

[Monitoramento e Comparação de Campanhas](https://igornascalves.github.io/projeto_ghanor/)


## Comparação de financiamento coletivo

![Primeiro Resultado - Gráficos](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/c96b0473-f59f-4170-92b2-f4d1e414ed97)


## Pontos Fortes para Engenharia de Dados
- **Orquestração:** Demonstra a habilidade de criar pipelines de dados eficientes com Apache Airflow.
- **Data Lake:** Estruturação e armazenamento de dados em camadas para análises futuras.
- **Automação:** Implementação de tarefas programadas e escaláveis.
- **Visualização:** Integração com ferramentas analíticas para geração de insights.

## Contato
[LinkedIn](https://www.linkedin.com/in/igor-nascimento-alves/) | [GitHub](https://github.com/IgorNascAlves)

