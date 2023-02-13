import requests
import json


cota_nome = []

for a in range(1,10):
    cotacoes = requests.get(f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/{a}')
    cotacoes = cotacoes.json()
    print(cotacoes[0]['bid'])
    cota_nome.append(cotacoes[0]['bid'])
    
print(cota_nome)