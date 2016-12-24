import locale
from math import sqrt, pow

n = int(input())

soma = 0

r5 = sqrt(5)
t1 = (1 + r5) / 2
t2 = (1 - r5) / 2

t1 = pow(t1, n)
t2 = pow(t2, n)

soma = t1 - t2
soma = soma / r5

print(locale.format("%.1f", soma))