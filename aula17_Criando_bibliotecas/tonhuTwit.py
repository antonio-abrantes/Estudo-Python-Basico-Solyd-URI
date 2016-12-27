import oauth2
import json
import pprint
import urllib.parse

class Twitter:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        try:
            self.conexao = self.conexao(consumer_key, consumer_secret, access_token, access_token_secret)
            print("Conexão estabelecida com sucesso\n")
        except Exception as e:
            print("Erro:", e)

#======================================================================================================================

    def conexao(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(access_token, access_token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

#======================================================================================================================

    def tweet(self, post):
        try:
            quary_codificada = urllib.parse.quote(post, safe="")
            requisicao = self.cliente.request("https://api.twitter.com/1.1/statuses/update.json?status=" + quary_codificada,
                                         method="POST")
            print("Tweet enviado com sucesso!")
        except:
            print("Erro de conexão...")

#======================================================================================================================

    def pesquisar(self, pesquisa):
        try:
            quary_codificada = urllib.parse.quote(pesquisa, safe="")
            requisicao = self.cliente.request(
                "https://api.twitter.com/1.1/search/tweets.json?q=" + quary_codificada + "&lang=pt")
            decodificar = requisicao[1].decode()

            resultado = json.loads(decodificar)

            print("LISTANDO RESULTADOS...")
            for twit in resultado["statuses"]:
                pprint.pprint(twit["user"]['screen_name'])
                pprint.pprint(twit["text"])
        except Exception as e:
            print("Erro", e)

#======================================================================================================================

    def op(self):
        try:
            op = int(input("Opção: "))
            return op
        except:
            print("Opção invalida")

#======================================================================================================================

    def menu(self):
        print(" ## OPÇÕES ##")
        print("1 - POSTAR TWEET")
        print("2 - PESQUISAR")
        print("0 SAIR")
        while True:
            op = self.op()
            if op == 0:
                print("Encerrar o sistema...")
                break
            if op == 1:
                post = input("Digite o tweet para postar: ")
                self.tweet(post)
            if op == 2:
                pesquisa = input("Pesquisa: ")
                self.pesquisar(pesquisa)
