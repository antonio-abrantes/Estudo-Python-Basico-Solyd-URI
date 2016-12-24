msg = input()
b = 0

for i in range(0, len(msg), 1):
    if(msg[i] == "1"):
        b = b + 1;

if(b % 2) == 0:
    print(msg+"0")
else:
    print(msg+"1")