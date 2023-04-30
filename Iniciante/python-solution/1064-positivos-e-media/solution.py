soma = 0
n_media = 0
for i in range(6):
    x = float(input())
    if x > 0:
        soma = soma + 1
        n_media = n_media + x
media = n_media / soma
print(f"{soma} valores positivos")
print(f"{media:.1f}")
