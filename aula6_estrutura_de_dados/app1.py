minsh_lista = ["Antonio", "Ana", "Fulano"]  #Lista

minha_tupla = ("Antonio", "Ana", "Fulano")  #Tupla

meu_dicionario = { 1: "Antonio", 2: "Ana", 3: "Fulano"} #Dicionario

meu_conjunto = {"Antonio", "Ana", "Fulano"}  #Conjunto

print(meu_dicionario[3])

nome = input("Digite o nome: ");

if nome in meu_conjunto:
    print("foi encontrado(a)!!")
else:
    print("Não foi encontrado(a)")