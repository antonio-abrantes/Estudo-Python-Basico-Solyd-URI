desejo = "Feliz natal!"

repet = int(input())
temp = ""

for i in range(0, len(desejo), 1):
    temp += desejo[i]
    if(i == 9):
        for j in range(0, repet-1, 1):
            temp += "a"

print(temp)