import locale
from math import log

n = float(input())

ans1 = n/log(n)
ans2 = (1.25506)*(n/log(n))

print(locale.format("%.1f", ans1), locale.format("%.1f", ans2))