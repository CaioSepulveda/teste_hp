# teste\_hp



1\. Visão Geral do Projeto

O objetivo principal deste projeto é demonstrar a capacidade de se conectar a um serviço externo via API REST, consumir seus dados e organizá-los em um formato utilizável. Especificamente, o projeto busca dados de previsão do tempo para uma cidade definida e os exporta para um arquivo Excel (.xlsx).



2\. API Utilizada

Devido à descontinuação do acesso gratuito à API da Climatempo para este tipo de uso, a integração foi realizada utilizando a OpenWeatherMap API.



Endpoint Principal: http://api.openweathermap.org/data/2.5/forecast



Dados Coletados: Previsão do tempo para os próximos 5 dias, com informações como temperatura, sensação térmica, umidade, descrição do clima e velocidade do vento.



Autenticação: Requer uma API Key gerada e ativada na plataforma OpenWeatherMap, que deve ser incluída como um parâmetro na requisição.



3\. Estrutura do Projeto e Tecnologias

O projeto é construído em Python e utiliza as seguintes bibliotecas:



requests: Essencial para fazer requisições HTTP para a API REST da OpenWeatherMap.



pandas: Utilizada para manipulação e organização dos dados extraídos da API em um DataFrame, facilitando a exportação.



openpyxl: Biblioteca necessária para que o pandas possa escrever e ler arquivos no formato .xlsx (Excel).







PARA EXECUTAR O SCRIPT

1 - Clone este Repositório

2 - Instale as bibliotecas python necessárias

3 - Obtenha sua API Key  em  https://openweathermap.org/.

4 - Configure o Script: 

Abra o arquivo teste\_hp.py

Substitua a API KEY pela sua (A presente no Script foi desativada)

Ajuste a variável Cidade

5 - Execute o Script Python









