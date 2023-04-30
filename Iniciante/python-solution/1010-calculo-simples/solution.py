l1 = input().split()
c1 = int(l1[0])
q1 = int(l1[1])
p1 = float(l1[2])

l2 = input().split()
c2 = int(l2[0])
q2 = int(l2[1])
p2 = float(l2[2])

valor = q1 * p1 + q2 * p2

print(f"VALOR A PAGAR: R$ {valor:.2f}")
