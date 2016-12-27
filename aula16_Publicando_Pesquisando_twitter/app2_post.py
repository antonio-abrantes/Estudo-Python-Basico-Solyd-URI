#Link da API - https://dev.twitter.com/rest/public
import oauth2
import json
import pprint
import urllib.parse


consumer_key =	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

try:
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    token = oauth2.Token(access_token, access_token_secret)

    cliente = oauth2.Client(consumer, token)

    quary = input("Novo tweet: ")
    quary_codificada = urllib.parse.quote(quary, safe="")

    requisicao = cliente.request("https://api.twitter.com/1.1/statuses/update.json?status="+quary_codificada, method="POST")
    print("Tweet enviado com sucesso!")
except:
    print("Erro no envio...")


