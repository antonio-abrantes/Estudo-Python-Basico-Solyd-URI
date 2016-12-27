import string
from datetime import datetime

def reverse1(texto):
    temp = []
    invert = texto.split()
    for item in invert:
        temp.append(item[::-1])
    return temp


texto = "O Rato Raul Roel a roupa do rei de roma"

print(texto[::-1])

a = string.ascii_letters
a = a[:26]
b = a[3:]

lista = reverse1(texto)

result = ""
for i in range(len(lista)):
    result += lista[i]
    if (i < len(lista)-1):#impedir que seja colocado espaço apos a ultima palavra
        result += " "

print(result)

result = string.Template("Erro: $alerta registrado em $data" ) #Exemplo de template

data = datetime.now()

dataCompleta = str(data.day)+"/"+ str(data.month)+"/" + str(data.year)

s = result.substitute({"alerta": "Perda de conexão", "data": dataCompleta})

print(s)

