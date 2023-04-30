x = float(input())

percentual = 0
if x <= 400.00:
    percentual = 15
elif x <= 800.00:
    percentual = 12
elif x <= 1200.00:
    percentual = 10
elif x <= 2000.00:
    percentual = 7
else:
    percentual = 4

salario = (x * percentual / 100) + x
reajuste = salario - x

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
