import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']['bid']

print(cotacoes_dolar)