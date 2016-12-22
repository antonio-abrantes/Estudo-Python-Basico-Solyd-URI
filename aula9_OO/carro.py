from aula9_OO.veiculo import Veiculo
class Carro(Veiculo):

    tipo = ""

    def __init__(self, cor, rodas, marca):
        Veiculo.__init__(self, cor, rodas, marca)
        self.tipo = "Carro"