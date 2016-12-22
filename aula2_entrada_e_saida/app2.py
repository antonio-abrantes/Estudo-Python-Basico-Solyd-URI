'''
EXERCICIO:
Faça um formulario que pergunte o nome, cpf, endereço, idade, altura e telefone
e imprimar esses valores em um relatorio organizado.
'''
print("Cadastro: Preencha os dados abaixo")

nome = input("Nome: ")
cpf = input("CPF: ")
endereco = input("Endereco: ")
idade = input("Idade: ")
altura = input("Altura: ")
telefone = input("Telefone: ")

print()
print("\tDADOS CADASTRADOS:")
print("\tNome:", nome, "CPF:", cpf, "\n\tEndereco: ", endereco)
print("\tIdade:", idade, "Altura:", altura, "m, Telefone:", telefone)
