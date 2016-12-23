'''
EXERCICIO:
Cada conta possui os atributos cliente, saldo e limite,
e os métodos sacar, depositar e consultar saldo.
'''

class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite


    def sacar(self, valor):
        if(valor > 0 and valor <= self.saldo):
            self.saldo -= valor
        else:
            if(valor > self.saldo or (self.saldo - valor < 0)):
                print("Saldo insuficiente")
            else:
                print("Valor menor ou igual a 0")


    def depositar(self, valor):
        if(valor != 0 and valor <= self.limite and valor > 0 and (self.saldo + valor) <= self.limite):
            self.saldo += valor
        else:
            if(valor > self.limite or (valor + self.saldo) > self.limite):
                print("Limite maximo atingido")
            elif(valor <= 0):
                print("Valor menor ou igual a 0")

    def consultarSaldo(self):
        print("Saldo atual R$", self.saldo)