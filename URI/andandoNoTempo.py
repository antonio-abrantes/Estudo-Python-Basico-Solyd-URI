a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if(a == b or b == c):
    print("S")
elif(a == b or c == a):
    print("S")
elif((b + c) == a or (b + a) == c or (c + a) == b):
    print("S")
else:
    print("N")