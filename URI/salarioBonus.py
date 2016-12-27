import locale

nome = input()
salario = float(input())
montante = float(input())

total_vendas = (montante * 15)/100

salario_final = salario + total_vendas

#printf("TOTAL = R$ %.2lf\n", salario_final);

print("TOTAL = R$ "+locale.format("%1.2f", salario_final))
