f1, f2 = map(float, input().split())

pib = (1 + (f1 / 100)) * (1 + (f2 / 100)) - 1

print(f"{pib*100:.6f}")
