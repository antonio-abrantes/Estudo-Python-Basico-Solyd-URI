def soma(num1, num2):#
  resp = num2 + num1
  return resp
#

a, b = input("Digite os numeros: ").split()

a = int(a)
b = int(b);

z = float(soma(a, b))

print(z)
