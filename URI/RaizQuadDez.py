import locale

repeticoes = int(input())
temp = 6

if repeticoes == 0:
    print(locale.format("%.10f", 3.0))
else:
    for i in range(1, repeticoes, 1):
        temp = float(6 + 1.0 / temp)

    temp2 = float(3 + 1 / temp)
    print(locale.format("%.10f",temp2 ))