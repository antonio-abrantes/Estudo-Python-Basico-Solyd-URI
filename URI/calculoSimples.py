import locale

pc1, n_pc1, v_pc1 = input().split()
pc1 = int(pc1)
n_pc1 = int(n_pc1)
v_pc1 = float(v_pc1)

pc2, n_pc2, v_pc2 = input().split()
pc2 = int(pc2)
n_pc2 = int(n_pc2)
v_pc2 = float(v_pc2)

valor_total = (n_pc1 * v_pc1) + (n_pc2 * v_pc2)

print("VALOR A PAGAR: R$ "+locale.format("%1.2f", valor_total))