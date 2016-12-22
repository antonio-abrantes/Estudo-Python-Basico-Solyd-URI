'''
EXERCICIO:
Faça um programa que leia a quantidade de pessoas que
serão convidados para uma festa.
Após isso, o programa irá perguntar o nome de todas as pessoas
e colocar em uma lista de convidados, e em seguida, irá imprimir
todos os nomes da lista.
'''
qtdPessoas = int(input("Quantidade de convidados: "))
lista_de_convidados = [];

for i in range(qtdPessoas):  #
    print("Convidado", i + 1, ":")
    nome = input("Nome: ")
    lista_de_convidados.append(nome)
    #
print("==================")
print("Lista:")
i = 1
for convidado in lista_de_convidados:
    print(str(i) + ": " + convidado)
    i += 1
print("==================")
