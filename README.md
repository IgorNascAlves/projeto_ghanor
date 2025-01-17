# Projeto: Monitoramento de Financiamento Coletivo - Jovem Nerd

## Descrição
Este projeto foi desenvolvido para monitorar e visualizar o progresso de campanhas de financiamento coletivo, como o do Jovem Nerd. Ele utiliza uma arquitetura robusta e ferramentas modernas para extrair, transformar e carregar dados de forma automatizada, permitindo análises avançadas e visualizações intuitivas. O objetivo é proporcionar insights detalhados sobre o desempenho das campanhas, auxiliando na tomada de decisões estratégicas e demonstrando competências fundamentais para engenharia de dados.

---

## Sobre o Projeto

### Arquitetura
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

### Tecnologias Utilizadas
- **Python:** Para desenvolvimento dos scripts de coleta e processamento de dados.
- **Apache Airflow:** Para orquestração dos pipelines de dados.
- **Flask:** Framework para desenvolvimento da aplicação web inicial.
- **Pandas:** Para manipulação e análise de dados.
- **Power BI:** Para criação de dashboards analíticos.
- **Data Lake:** Implementado localmente para armazenamento de dados estruturados e não estruturados.

### Funcionalidades
- **Extração de Dados:** Coleta de informações da API do financiamento coletivo.
- **Armazenamento em Data Lake:** Dados salvos em camadas (bronze, silver) para garantir histórico e integridade.
- **Pipeline Automatizado:** Orquestração diária utilizando Apache Airflow.
- **Visualizações Avançadas:** Dashboards interativos no Power BI para análise do desempenho da campanha.
- **Histórico de Arrecadação:** Rastreio do progresso da campanha em tempo real.

---

## Análises e Aplicações

### Análise Power BI

![Análise Power BI - Visão Geral](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/f9018c10-f129-43eb-903e-2d7378c6d06f)

![Análise Power BI - Detalhes](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/c9a60fbe-f1ec-4f14-a9f3-82b1392ee812)

### Aplicação

![Aplicação - Dashboard Inicial](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/2a95c9bf-0045-4c56-967a-65f6ce1ef078)

### Comparação de Campanhas
Explore os dados e análises comparativas diretamente na página abaixo:

[Monitoramento e Comparação de Campanhas](https://igornascalves.github.io/projeto_ghanor/)

### Comparação de Financiamento Coletivo

![Primeiro Resultado - Gráficos](https://github.com/IgorNascAlves/projeto_ghanor/assets/26041581/c96b0473-f59f-4170-92b2-f4d1e414ed97)

Os gráficos mostram o desempenho das campanhas ao longo do tempo, comparando métricas como arrecadação diária, acumulada e metas atingidas. Isso oferece insights valiosos sobre a eficácia de estratégias de engajamento e impacto das ações realizadas.

---

## Conclusão

### Análise do Gráfico de Desempenho das Campanhas

O gráfico analisado demonstra a variação do total arrecadado ao longo do tempo, comparando três campanhas de financiamento coletivo: **Ordem Paranormal**, **Coleção Cthulhu** e **Tesouros de Ghanor**. As principais observações são:

1. **Comportamento Geral:**
   - Há um pico significativo de arrecadação nos primeiros dias de todas as campanhas, mostrando a importância do engajamento inicial.
   - Após o pico inicial, a arrecadação diminui rapidamente e se estabiliza, com um leve aumento nos dias finais.

2. **Comparação entre os Projetos:**
   - **Tesouros de Ghanor** teve o maior pico inicial, atingindo cerca de 4 milhões no primeiro dia, mas apresentou uma queda acentuada nos dias seguintes.
   - **Coleção Cthulhu** destacou-se com um crescimento expressivo no final da campanha, possivelmente devido a uma comunicação eficaz e estratégias para estimular contribuições tardias.
   - **Ordem Paranormal** apresentou um desempenho mais estável, com menos variações extremas ao longo do período.

3. **Padrões Identificados:**
   - **Engajamento Inicial e Final:** O início e o fim das campanhas são os períodos mais críticos para maximizar a arrecadação.
   - **Diferença entre Projetos:** Estratégias diferentes resultaram em picos em momentos distintos, indicando oportunidades para ajustes táticos durante a campanha.

### Insights para o Futuro
- **Engajamento Contínuo:** É essencial manter o interesse dos apoiadores no período intermediário da campanha, utilizando atualizações frequentes e incentivos.
- **Senso de Urgência no Final:** A utilização de estratégias que gerem urgência nos últimos dias pode elevar significativamente os valores arrecadados.
- **Comparação de Estratégias:** A análise comparativa permite identificar boas práticas e ajustar as campanhas futuras para alcançar resultados ainda melhores.

---

## Contato
[LinkedIn](https://www.linkedin.com/in/igor-nascimento-alves/) | [GitHub](https://github.com/IgorNascAlves)

