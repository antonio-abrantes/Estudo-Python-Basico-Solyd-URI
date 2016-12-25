import re
import requests
import json

# Site para montar expressões regulares - https://regex101.com/
def requisicao(endereco, expressao):
    expresao = "[\w-]+@[\w-]+\.[\w\.-]+"  # verificar se uma string digitada corresponde a um email valido

    try:
        texto = requests.get(endereco)
        string = texto.text

        achou = re.findall(expresao, string)

        if (achou):
            print("E-mail encontrado!")
            print("E-mail encontrado:", achou[0])
        else:
            print("Nao eh encontrado!")

    except Exception as e:
        print(e.args)


expresao = "[\w-]+@[\w-]+\.[\w\.-]+"  # verificar se uma string digitada corresponde a um e-mail valido

#ebdereço buscado pode ser definido atraves de um input()
endereco = "http://lacoxinha.com.br/contato"

requisicao(endereco, expresao)

string_teste = "o gato é@bonitas demais, a gata, os gatinhos, os gatos"
#teste = input()
#padrao = re.search(teste+"+", string_teste)  # r = RAW String
padrao = re.findall(r"[gat]+", string_teste)

if padrao:
    #print(padrao.group())
    print(padrao)
else:
    print("Padrão não encontrado")