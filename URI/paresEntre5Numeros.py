qtd = 0

for i in range(5):
    val = int(input())
    if(val % 2) == 0:
        qtd = qtd + 1

print(qtd, "valores pares")