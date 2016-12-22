import locale

num1 = float(input())
num2 = float(input())
num3 = float(input())

MEDIA = (num1 * 2 + num2 * 3 + num3 * 5) / 10

print("MEDIA =", locale.format("%1.1f", MEDIA))