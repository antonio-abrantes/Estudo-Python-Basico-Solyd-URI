ciclos = int(input())

while ciclos > 0:
    h, m, caso = input().split()

    h = int(h)
    m = int(m)
    caso = int(caso)
    hora = ""

    if h < 10:
        hora = "0"+str(h)+":"
        if m < 10:
            hora += "0"+str(m)+" - "
        else:
            hora += str(m)+" - "

        if(caso == 1):
            print(hora+"A porta abriu!")
        else:
            print(hora + "A porta fechou!")
    else:
        hora = str(h) + ":"
        if m < 10:
            hora += "0"+str(m)+" - "
        else:
            hora += str(m)+" - "

        if (caso == 1):
            print(hora + "A porta abriu!")
        else:
            print(hora + "A porta fechou!")

    ciclos -= 1