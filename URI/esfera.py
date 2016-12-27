import locale
pi = 3.14159

raio = float(input())

raio3 = (raio * raio) * raio
volume = (4/3.0) * pi * raio3

print("VOLUME = "+locale.format("%1.3f", volume))