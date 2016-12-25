import requests
import json

def requisicao():
    try:
        nome = input("Nome do filme: ")
        nome = str.lower(nome)
        busca = []
        cont = 0
        for i in range(1, 1000):
            try:
                req = requests.get("http://www.omdbapi.com/?s=" + nome + "&type=movie&page=" + str(i))
                teste = json.loads(req.text)
                if (teste["Response"] == "False"):
                    break
                else:
                    for filme in teste["Search"]:
                        busca.append(filme)
                        cont += 1
                    '''
                    busca.append(json.loads(req.text))
                    cont += 1
                    '''
            except:
                print("Erro na requisição...")

        print("Quantidade de resultados: " + str(cont))
        for i in range(cont):
            print("Nome: " + busca[i]["Title"])
            print("Ano: " + busca[i]["Year"])
            try:
                print("Atores princiapis: " + busca[i]["Actors"])
            except:
                print("Não definido")
            print("Poster: " + busca[i]["Poster"])

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