#Link da API - https://dev.twitter.com/rest/public
import oauth2
import json
import pprint
import urllib.parse


consumer_key =	"WDsEyiugPHG6nSRAB3laRtoBD"
consumer_secret = "KIvJv65fGk03JVLeojRaeRUUZmK5nrSa76BIm60VmPK6uljqIy"
access_token = "321997268-4xy8FnAUobMLcnr7n67najLElYzB99P4tGK9DQhv"
access_token_secret = "sgs1ha6AOOopBpZ5FB4dWg35PV97j7OcjXJ6ne1mam4Ef"

try:
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    token = oauth2.Token(access_token, access_token_secret)

    cliente = oauth2.Client(consumer, token)

    quary = input("Pesquisa: ")
    quary_codificada = urllib.parse.quote(quary, safe="")

    requisicao = cliente.request("https://api.twitter.com/1.1/search/tweets.json?q="+quary_codificada+"&lang=pt")
    decodificar = requisicao[1].decode()

    resultado = json.loads(decodificar)

    #print(resultado["statuses"])
    for twit in resultado["statuses"]:
        pprint.pprint(twit["user"]['screen_name'])
        pprint.pprint(twit["text"])

except:
    print("Erro de conexão")