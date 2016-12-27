#Link da API - https://dev.twitter.com/rest/public
import time
import oauth2
import json
import pprint
import urllib.parse

def postar(post, cliente):
    try:
        quary_codificada = urllib.parse.quote(post, safe="")
        requisicao = cliente.request("https://api.twitter.com/1.1/statuses/update.json?status=" + quary_codificada,
                                     method="POST")
        print("Tweet enviado com sucesso!")
    except:
        print("Erro de conexão...")



consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(access_token, access_token_secret)

cliente = oauth2.Client(consumer, token)

post1 = "elefantes incomodam muita gente"
post2 = ""

i = 1
while True:
    if(i == 1):
        primeiro = "1 elefante incomoda muita gente"
        postar(primeiro, cliente)
        print(primeiro)
        i = i + 1
        time.sleep(2)
        continue
    if(i % 2) != 0:
        string = str(i)+" "+post1
        print(string)
        postar(string, cliente)
    else:
        concat = ""
        for j in range(i):
            concat += " incomodam"
        if(len(concat) >= 140):
            postar("Agora acabou mesmo =P", cliente)
            break
        post2 = str(i) + " elefantes" + concat + " muito mais"
        print(post2)
        postar(post2, cliente)
    i = i + 1
    time.sleep(2)