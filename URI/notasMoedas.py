import locale

n = [10000,5000,2000,1000,500,200]
m = [100,50,25,10,5,1]

rest = float(input())

cents = rest * 100

#NOTAS
print("NOTAS:")
for i in range(len(n)):
    print(int(cents / n[i]), "nota(s) de R$",locale.format("%1.2f", n[i] / 100));
    cents = cents % n[i]

print("MOEDAS:");
for i in range(len(m)):
    print(int(cents / m[i]), "moeda(s) de R$", locale.format("%1.2f", m[i] / 100));
    cents = (cents) % m[i];