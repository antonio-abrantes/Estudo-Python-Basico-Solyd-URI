a = int(input())
b = int(input())

somaImpares = 0

if(a < b):
    i = a + 1
    while i < b:
        if(i % 2) != 0:
            somaImpares = somaImpares + i
        i += 1
    print(somaImpares)
elif(a > b):
    i = b + 1
    while i < a:
        if(i % 2) != 0:
            somaImpares = somaImpares + i
        i += 1
    print(somaImpares)
else:
	print(somaImpares)