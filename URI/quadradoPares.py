from math import pow

n = int(input())

i = 1

while i <= n:
    if(i % 2) == 0:
        print(str(i)+"^2 =", int(pow(i, 2)))
    i += 1