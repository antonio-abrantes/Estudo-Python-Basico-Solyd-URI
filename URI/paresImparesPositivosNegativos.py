somaPares = 0
somaImpar = 0
somaPosi = 0
somaNeg = 0

i = 0
while i < 5:
    val = int(input())

    if (val > 0):
        somaPosi += 1

    if (val < 0):
        somaNeg += 1

    if ((val % 2) == 0):
        somaPares += 1

    else:
        somaImpar += 1

    i += 1

print(somaPares, "valor(es) par(es)")
print(somaImpar, "valor(es) impar(es)")
print(somaPosi, "valor(es) positivo(s)")
print(somaNeg, "valor(es) negativo(s)")