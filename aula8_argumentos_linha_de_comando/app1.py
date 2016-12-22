import sys

argumento = sys.argv

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return abs(num1 - num2)

if(argumento[1] == "soma"):
    resp = soma(int(argumento[2]), int(argumento[3]))
elif(argumento[1] == "sub"):
    resp = sub(int(argumento[2]), int(argumento[3]))

print(resp)