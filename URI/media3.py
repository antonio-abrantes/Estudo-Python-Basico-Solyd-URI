import locale

n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

m = float(((n1 * 2.0) + (n2 * 3.0) + (n3 * 4.0) + (n4 * 1.0)) / 10.0)

print("Media:", locale.format("%.1f", m))
print("Media:", locale.format("%.3f", m))
if (m >= 7.0):
    print("Aluno aprovado.")

elif (m < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaex = float(input("Nota do exame: "))
    mF = float((m + notaex) / 2.0)
    if (mF >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final:", locale.format("%.1f", mF))
