import requests
import json
from datetime import datetime
from time import time;


start_date = int(input("data que você quer saber: "))
end_date = start_date
all_cotations = []
#for d in range(0,2):
cotacoes = requests.get(f'https://economia.awesomeapi.com.br/USD-BRL/1?start_date={start_date}&end_date={end_date})')
cotacoes = cotacoes.json()
cotation = cotacoes[0]['bid']
data_completa = cotacoes[0]['timestamp']
data_completa = time()
data_completa = (datetime.utcfromtimestamp(data_completa).strftime('%d/%m/%Y'))
all_cotations.append([data_completa, cotation])
#end_date += 1
#start_date += 1


print(all_cotations)
#for datacota in range(1,10):
 #   print(f'A cotação do dia {all_cotations[datacota][0]} foi de R$ {all_cotations[datacota][1]}')