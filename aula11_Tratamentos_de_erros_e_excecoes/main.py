import time

def abre_arquivo():
    try:
        arquivo = open("arquivo.txt", "r")
        return arquivo
    except  Exception as e:
        print("Erro:", e)
        return False

if(abre_arquivo() != False):
    print("Abriu o arquivo!")
else:
    print("Fluxo do sistema continua...")
    nome = input("Qual seu nome? ")
    print("Bom trabalho", nome + "!")

