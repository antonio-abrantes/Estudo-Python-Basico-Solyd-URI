import locale
pi = 3.14159
A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

triangulo = (A * C)/2;

circulo = pi *(C * C);

trapezio = ((A + B)*C)/2

quadrado = B * B;

retangulo = A * B;

print("TRIANGULO:", locale.format("%1.3f", triangulo));
print("CIRCULO:", locale.format("%1.3f", circulo));
print("TRAPEZIO:", locale.format("%1.3f", trapezio));
print("QUADRADO:", locale.format("%1.3f", quadrado));
print("RETANGULO:", locale.format("%1.3f", retangulo));