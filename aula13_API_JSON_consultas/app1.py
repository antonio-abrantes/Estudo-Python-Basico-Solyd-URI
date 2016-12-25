import requests
import json

def requisicao():
    try:
        nome = input("Nome do filme: ")
        nome = str.lower(nome)
        req = requests.get("http://www.omdbapi.com/?t=" + nome)
        busca = json.loads(req.text)
        print("Nome:", busca["Title"], "- Ano:", busca["Year"], "- Atores princiapis:", busca["Actors"], "\nLink do poster:", busca["Poster"])
    except Exception as e:
        print("Filme não localizado")


sair = False
print("Opções: [sair/buscar]")
while not sair:
    op = input("Opção: ")
    op = str.lower(op)

    if(op == "sair"):
        sair = True
    elif(op == "buscar"):
        requisicao()
    else:
        print("Opção invalida")