'''
EXERCICIO: Crie um software de gerenciamento bancário.
Esse software poderá ser capaz de criar clientes e contas.
'''
from aula9_OO.cleinte import Cliente
from aula9_OO.conta import Conta

def menuPrincipal():
    print("   #Opções")
    print("1 - Nova Conta")
    print("2 - Listas Clientes")
    print("3 - Buscar cliente")
    print("0 - Sair")

def menuCliente(conta):
    print("  #Opções do Cliente")
    print("1 - Sacar")
    print("2 - Depositar")
    print("0 - Sair")
    while True:
        conta.consultarSaldo()
        opC = int(input("Opção: "))
        if(opC == 1):
            valor = float(input("Sacar: "))
            conta.sacar(valor)
        elif(opC == 2):
            valor = float(input("Depositar: "))
            conta.depositar(valor)
        elif(opC == 0):
            print("Retornar ao menu principal")
            menuPrincipal()
            break;
        else:
            print("Opção invalida")

contas = []

menuPrincipal()

while True:
    op = int(input("Digite a opção: "))
    if(op == 1):
        print("Abrir nova conta")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        saldo = float(input("Deposito inicial: "))
        limite = float(saldo + (saldo * 25) / 100)
        clienteNovo = Cliente(nome, cpf, idade)
        contaNova = Conta(clienteNovo, saldo, limite)
        contas.append(contaNova)
    elif(op == 2):
        for conta in contas:
            print("Nome:", conta.cliente.nome)
            conta.consultarSaldo()
            print("Limite atual: R$",conta.limite)
    elif(op == 3):
        buscar = input("Nome do cliente: ")
        achou = 0
        for conta in contas:
            if (conta.cliente.nome == buscar):
                achou = 1
                menuCliente(conta)
                break
        if(achou == 0):
            print("Cliente não encontrado")
    elif(op == 0):
        print("Encerrando o sistema...")
        break
    else:
        print("Opção invalida")