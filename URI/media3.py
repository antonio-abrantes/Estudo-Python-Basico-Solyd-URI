import locale

n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

m = float(((n1*2) + (n2*3) + (n3*4) + (n4*1))/10)

print("Media:", locale.format("%1.1f", m))

if (m >= 7):
     print("Aluno aprovado.")

elif(m < 5):
     print("Aluno reprovado.")
elif(m >= 5 and m < 7):
    print("Aluno em exame.")
    notaex = float(input("Nota do exame: "))
    m = float((m + notaex)/2)
    if(m >= 5):
       print("Aluno aprovado.")
    else:
       print("Aluno reprovado.")

    print("Media final:",locale.format("%1.1f", m))
