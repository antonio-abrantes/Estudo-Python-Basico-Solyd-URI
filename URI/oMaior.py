
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b))/2.0

if(maiorAB < c):
    print(int(c),"eh o maior")
else:
    print(int(maiorAB),"eh o maior")
