import requests
import json
import pandas as pd
from datetime import datetime
from time import time

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/5')
cotacoes = cotacoes.json()
#data = cotacoes['USDBRL']['timestamp']
#data = time()
#cotacoes['USDBRL']['timestamp'] = datetime.utcfromtimestamp(data).strftime('%d/%m/%Y')

df = pd.DataFrame.from_dict(cotacoes)

print(df.fillna(method="ffill"))

