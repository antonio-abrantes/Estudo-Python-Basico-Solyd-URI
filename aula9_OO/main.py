from aula9_OO.veiculo import Veiculo
from aula9_OO.carro import Carro

caminhao_rosa = Veiculo("Rosa", 6, "Ford")
carro_azul = Carro("Azul", 4, "Fiat")

print("Caminhão:", caminhao_rosa.cor)
print("Marca:", caminhao_rosa.marca)
print("Qtd rodas:", caminhao_rosa.rodas)
caminhao_rosa.ligar(True)
caminhao_rosa.acelerar()

print("================================")
print(carro_azul.tipo, carro_azul.cor)
print("Marca:", carro_azul.marca)
print("Qtd rodas:", carro_azul.rodas)

carro_azul.ligar(False)
carro_azul.acelerar()
