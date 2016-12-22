lim1 = 0
lim2 = 25
lim3 = 50
lim4 = 75
lim5 = 100

num = float(input())

if (num >= lim1 and num <= lim2):
    print("Intervalo [0,25]")
elif (num >= lim2 and num <= lim3):
    print("Intervalo (25,50]")
elif (num >= lim3 and num <= lim4):
    print("Intervalo (50,75]")
elif (num >= lim4 and num <= lim5):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
