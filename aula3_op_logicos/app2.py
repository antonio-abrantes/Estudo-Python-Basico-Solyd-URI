'''
Exercicio:
Faça um programa que pergunte a idade, o peso e altura
e decide se a pessoa esta apta a ser do exercito
Obs: Para estar apta, é preciso ter mais de (>=)18 anos, mais de (>=)60 kilos
e mais de (>=)1.70 de altura
'''
print("CADASTRO DO EXERCITO")
idade = int(input("Idade: "))
peso = float(input("Peso: "))
altura = float(input("Altura: "))

if(idade >= 18 and peso >= 60 and altura >= 1.70):
    print("A pessoa com os dados cadastrados esta apta servir ao exercito")
else:
    print("Não apto")


