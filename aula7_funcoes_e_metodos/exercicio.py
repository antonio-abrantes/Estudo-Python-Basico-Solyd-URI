'''
EXERCICIO:
Escreva uma função que recebe um objeto coleção e
retorna o valor do maior numero dentro dessa coleção,
e em seguida, outra que retorna no menor numero.
'''
def maiorNum(lista): #
    maior = lista[0]
    for i in range(len(lista)):
        if (lista[i] > maior):
            maior = lista[i]
    return maior
#

def menorNum(lista): #
    menor = lista[0]
    for i in range(len(lista)):
        if (lista[i] < menor):
            menor = lista[i];
    return menor
#

lista = [10, 20, 15, 88, 17, 96, 110, 111, 8, 1, -22]

maior = maiorNum(lista)

print("\nO maior numero da lista é:", maior)

menor = menorNum(lista)

print("O menor numero da lista é:", menor)
