def operacoes(dicionario):

    soma = sum(dicionario.values())

    media = soma / len(dicionario.values())

    variacao = max(dicionario.values()) - min(dicionario.values())
    return soma, media, variacao

#dicionario = {1: 8, 2: 10, 3: 8 }
dicionario = {'laranjas': 525, 'abacaxis': 430, 'bananas': 312}

result = operacoes(dicionario)

print(len(result))
print(result)

print(dicionario["laranjas"])
