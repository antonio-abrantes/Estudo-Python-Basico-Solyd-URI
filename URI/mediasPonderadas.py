import locale
n = int(input())

while n > 0:
    med1, med2, med3 = input().split()
    med1 = float(med1)
    med2 = float(med2)
    med3 = float(med3)

    mediaGeral = float((med1 * 2 + med2 * 3 + med3 * 5) / 10.0)

    print(locale.format("%.1f", mediaGeral))
    n -= 1