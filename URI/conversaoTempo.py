import locale
N = int(input())

segundos = int((N % 3600) % 60)
minutos = int((N % 3600) / 60)

if(N < 3600):
    horas = 0
else:
    horas = N / 3600

print(str(int(horas))+":"+ str(minutos)+":"+ str(segundos))