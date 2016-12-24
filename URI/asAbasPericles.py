nAbas, acoes = input().split()

nAbas = int(nAbas)
acoes = int(acoes)

while acoes > 0:

    acao = input()

    if(acao == "fechou"):
        nAbas = nAbas - 1
        nAbas = nAbas + 2

    if(acao == "clicou"):
        nAbas = nAbas - 1

    acoes = acoes - 1

print(nAbas)