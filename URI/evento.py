import locale

while True:
    try:
        qtd, entrada = input().split()
        qtd = int(qtd)
        entrada = float(entrada)

        if (qtd + entrada) == 0:
            break

        multiplica = float(qtd * entrada)

        print(locale.format("%.0f", multiplica))
    except:
        break

