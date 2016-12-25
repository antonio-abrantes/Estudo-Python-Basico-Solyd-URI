import requests
import json
import time
from datetime import datetime

def requisicao():
    now = datetime.now()
    print("Data atual: "+ str(now.day)+"/"+str(now.month)+"/"+str(now.year))
    print("  ### COTAÇÃO ###")
    while True:
        try:
            dados = []
            req = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
            busca = json.loads(req.text)
            dados.append(busca["valores"]["USD"])
            print("Moeda:", dados[0]["nome"], "\nValor atual: U$", dados[0]["valor"])
            dados.append(busca["valores"]["EUR"])
            print("Moeda:", dados[1]["nome"], "\nValor atual: U$", dados[1]["valor"])
            dados.append(busca["valores"]["BTC"])
            print("Moeda:", dados[2]["nome"], "\nValor atual: U$", dados[2]["valor"])
            time.sleep(5)
            print("=============================")
        except Exception as e:
            print("Erro de conexão")
            break

requisicao()