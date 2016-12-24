import locale

repeticoes = int(input())
temp = 2

if repeticoes == 0:
    print(locale.format("%.10f", 1.0))
else:
    for i in range(1, repeticoes, 1):
        temp = float(2 + 1.0 / temp)

    temp2 = float(1 + 1 / temp)
    print(locale.format("%.10f",temp2 ))