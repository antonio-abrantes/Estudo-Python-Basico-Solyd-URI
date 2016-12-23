tmp = 0

n = int(input())

i = 0
while i < n:
    x = int(input())
    if(x >= 10 and x <= 20):
        tmp += 1
    i += 1
print(tmp, "in")
print((n - tmp), "out")