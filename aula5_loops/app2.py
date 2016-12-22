while True:
    a = int(input("1º Valor: "))
    b = int(input("2º Valor: "))

    print(a + b)
    resp = input("Deseja continuar? [s/n]: ")
    if resp not in('s'):
        break


