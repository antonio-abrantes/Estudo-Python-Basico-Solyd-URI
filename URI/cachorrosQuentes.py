import locale

qtdC, qtdA = input().split()

qtdC = float(qtdC)
qtdA = float(qtdA)

result = qtdC / qtdA

print(locale.format("%.2f", result))