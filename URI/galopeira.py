import locale

ciclos = int(input())

while ciclos > 0:
    galopeira = input()
    qtd = len(galopeira)

    tempo = float(qtd / 100)
    print(locale.format("%.2f", tempo))
    ciclos -= 1
