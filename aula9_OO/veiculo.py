class Veiculo:

    ligado = False;

    def __init__(self, cor, rodas, marca):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca

    def ligar(self, estado):
        self.ligado = estado;
        if(estado == True):
            print("Veiculo esta ligado")
        else:
            print("Veiculo esta desligado")

    def acelerar(self):
        if(self.ligado == True):
            print("Veiculo esta acelerando")
        else:
            print("Não é possivel acelerar\nMotivo: É necessario ligar o veiculo primeiro")