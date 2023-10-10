# Diário do Projeto: Acompanhamento do Financiamento Coletivo do Jovem Nerd

## Dias
- [Dia 1](/jornal.md/#Dia-1)

## Dia 1

**Data:** 09/10/2023

**Resumo:**
Na sexta-feira passada, em 06/10/2023, o Jovem Nerd iniciou seu segundo financiamento coletivo, marcando outro sucesso notável. Desta vez, optaram por criar sua própria plataforma em vez de utilizar o Catarse como fizeram na primeira vez. Rapidamente, a campanha atingiu a marca de 3 milhões de reais arrecadados. ([ghanor.com.br](https://ghanor.com.br/))

**Motivação:**
Ao acompanhar o progresso da campanha, senti falta da facilidade de visualização oferecida pela plataforma do [Catarse](https://www.catarse.me/nerdcastrpg?ref=ctrse_explore_pgsearch#contributions), que incluía gráficos informativos. Para resolver essa questão, decidi criar uma solução personalizada para monitorar e visualizar o progresso da campanha.

**Abordagem Técnica:**
- Explorei a página da campanha e descobri que havia uma API que fornecia informações atualizadas sobre o valor arrecadado.
- Criei um código em Python que periodicamente lê os dados da API e atualiza um arquivo CSV sempre que o valor arrecadado muda. Isso me permite rastrear o histórico de arrecadação.
- Desenvolvi uma aplicação web usando Flask que utiliza esses dados para gerar um gráfico e uma tabela.

**Expansão do Projeto:**
No entanto, a aplicação de monitoramento que criei parava de rodar sempre que atualizava a analise. Para resolver isso, decidi implementar uma solução mais robusta.
- Utilizei o Apache Airflow para criar uma tarefa que, a cada minuto, faz a extração dos dados da API e os armazena em um "lake" de dados bruto.
- Essa abordagem me permitirá explorar os dados com mais flexibilidade no futuro e criar visualizações mais avançadas.

Com essas atualizações, o projeto está se tornando mais robusto e eficaz no acompanhamento do financiamento coletivo do Jovem Nerd. Continuarei a aprimorar e expandir essa solução à medida que o projeto avança.

**Sugestões**

Conversando com os meus amigos, ViS3C e Gui, recebi algumas sugestões incríveis para o meu projeto. Duas delas se destacaram:

1. Coletar dados de campanhas anteriores, como a do Jovem Nerd e do Cellbit, para obter insights valiosos. Felizmente, o Catarse disponibiliza informações detalhadas sobre o desempenho das campanhas, o que facilitará a análise.

2. Registrar as datas em que o Jovem Nerd realizou ações para engajar a campanha, como posts no Instagram e transmissões ao vivo no YouTube, e analisar o impacto dessas atividades. Embora essa parte do projeto envolva um trabalho manual, acreditamos que os resultados valerão a pena.

Estou empolgado para colocar essas sugestões em prática e continuar a aprimorar o meu projeto.
