# Extract
import requests #biblioteca para acesso à API
import json     #biblioteca para manipulação de json

SDW2023_API_URL = 'https://sdw-2023-prd.up.railway.app' #endereço da API
response = requests.get(f'{SDW2023_API_URL}/users')     #recuperando todos os registros de usuários

if response.status_code != 200:           #caso ocorra algum erro, o programa é finalizado
    print('Erro ao acessar os dados!')
    exit()

#transformando o retorno da API em uma lista de usuários
users_list = list(response.json())

# Transform

#Filtrando usuários que ainda não possuem nenhuma notícia
users_without_news = [user for user in users_list if (len(user['news'])) == 0]
users_without_news

# Load

#Preparando um arquivo csv com os dados dos usuários filtrados
RESULTS_FILE = 'SDW2023.csv'
try:
    with open(RESULTS_FILE, 'w') as file:
        file.write('UserID\n')
        for user in users_without_news:
          file.write(str(user['id']) + '\n')
except Exception as e:
    print(e)