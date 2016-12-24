maior = 0
cont_posi = None

for i in range(0, 5, 1):
    num = int(input())
    if(num > maior):
        maior = num
        cont_posi = i + 1


print(maior)
print(cont_posi)