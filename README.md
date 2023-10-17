# dio-lab-pipeline-ETL
 Desafio de projeto desenvolvido durante o Bootcamp de Ciência de Dados com Python ofertado pela DIO em parceria com o Santander.

 ## Descrição
Este projeto é uma continuação do [Santander Dev Week 2023 (ETL com Python)](https://colab.research.google.com/drive/1SF_Q3AybFPozCcoFBptDSFbMk-6IVGF-?usp=sharing).

O código carrega todas as intâncias de usuários disponíveis na [API RESTful da DIO](https://github.com/digitalinnovationone/santander-dev-week-2023-api). Após isso, são identificados todos os usuários que ainda não receberam nenhuma notícia personalizada. Por fim, o programa cria um arquivo csv (SDW2023.csv) com os ids desses usuários.

A ideia desse código é que ele gere uma lista de usuários que pode ser consumida pelo processo de ETL desenvolvido pela DIO e aí sim enviar as notícias aos usuários!
