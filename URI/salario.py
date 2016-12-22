import locale

num_func = int(input())
num_hora = int(input())
valor_r = float(input())

salario = num_hora * valor_r

print("NUMBER =", num_func)
print("SALARY = U$", locale.format("%1.2f", salario))