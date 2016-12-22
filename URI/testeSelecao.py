A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B > C and D > A):
    somaCD = C + D
    somaAB = A + B
    # Teste 2 - soma de C com D for maior que a soma de A e B
    if (somaCD > somaAB):
        # Teste 3 - C e D, ambos, forem positivos
        if C >= 0 and D >= 0:
            if (A % 2) == 0:
                print("Valores aceitos")
            else:
                print("Valores ncao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
