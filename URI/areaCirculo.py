import locale

pi = 3.14159

raio = float(input())

raio = raio * raio

area = pi * raio

print("A="+ locale.format("%1.4f", area))