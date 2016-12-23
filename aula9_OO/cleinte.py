'''
EXERCICIO:
Cada clinte possui, nome, cpf e idade
Cada conta possui os atributos cliente, saldo e limite,
e os métodos sacar, depositar e consultar saldo.
'''
class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade