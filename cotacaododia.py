import requests
import json
from datetime import datetime
from time import time;

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
cotacoes = cotacoes.json()
data = cotacoes['USDBRL']['timestamp']
#data = time()
print(type(data))
#print(datetime.utcfromtimestamp(data).strftime('%d/%m/%Y'))

#print(cotacoes_dolar)