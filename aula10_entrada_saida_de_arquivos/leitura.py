import random

with open('alunos.txt', 'r') as f:
	alunos = f.readlines()
	print(random.choice(alunos))


with open('alunos.txt', 'a') as f:
    alunos = input("Digite o nome: ")
    alunos += "\n"
    f.writelines(alunos)

arquivo = open('alunos.txt', 'r')

lista = arquivo.read()

print(type(lista))

for linha in arquivo:
    print(linha)


