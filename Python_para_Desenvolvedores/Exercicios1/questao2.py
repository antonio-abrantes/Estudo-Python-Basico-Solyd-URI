'''
Considerando que qualquer numero é divisivel por 1 e por ele mesmo, e apos
o numero 1 e antes do numero em questão, qualquer numero só tera divisão exata
até no maximo sua metade, sendo assim, dividindo o numero por 2 e colocando o numero
resultante + 1 como limite, as interações são consideravelmente redizidas
'''

def eh_primo(num):
    temp = int((num / 2) + 1)
    for i in range(2, temp, 1):
        if(num % i) == 0:
            return False
    return True

while True:
    num = int(input("Digite o numero: "))

    if(num == 0):
        break

    resp = eh_primo(num)

    if (resp == False):
        print("Não é primo")
    else:
        print("É primo")