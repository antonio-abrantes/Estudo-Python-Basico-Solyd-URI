import locale
x = int(input())
y = float(input())

consumoMedio = x / y

print(locale.format("%1.3f", consumoMedio),"km/l")