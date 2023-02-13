import requests
import json

start_date = 20230201
days = int(input("Quantos dias mais você gostaria de saber a cotação [1-20]: "))
end_date = start_date + days
all_cotations = []
for d in range(start_date,end_date):
    cotacoes = requests.get(f'https://economia.awesomeapi.com.br/USD-BRL/10?start_date={start_date}&end_date={end_date})')
    cotacoes = cotacoes.json()
    cotation = cotacoes[0]['bid']
    start_date = str(start_date)
    dia = start_date[6:9]
    mes = start_date[4:6]
    ano = start_date[0:4]
    data_completa = f'{dia} / {mes} / {ano}'
    all_cotations.append([data_completa, cotation])
    start_date = int(start_date)
    end_date += 1
    start_date += 1
    
for datacota in range(0,(end_date - start_date)):
    print(f'A cotação do dia {all_cotations[datacota][0]} foi de R$ {all_cotations[datacota][1]}')