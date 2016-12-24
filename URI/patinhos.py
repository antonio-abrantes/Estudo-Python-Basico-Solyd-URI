import locale

while True:
    try:
        patinho = float(input())
        if (patinho == -1):
            break;

        if(patinho == 0):
            print(locale.format("%.0f", patinho))
        else:
            cont = patinho
            while cont > 0:
                print(locale.format("%.0f", (cont -1)))
                cont = cont - 1
                break
    except:
        break
