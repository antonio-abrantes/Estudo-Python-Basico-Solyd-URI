import locale

qtd = 0
val = 0.0
soma = 0.0

for i in range(6):
    val = float(input())
    if(val >= 0):
        qtd = qtd + 1
        soma += val

print(qtd, "valores positivos")
print(locale.format("%1.1f", float(soma/float(qtd))))