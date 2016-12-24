ciclos = int(input())

while ciclos > 0:

    lim = int(input())
    soma = 0
    temp = 1

    for i in range(0, lim, 1):
        soma = temp * 2
        temp = soma

    print((soma -1))

    ciclos -= 1