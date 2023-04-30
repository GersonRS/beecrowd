valores = input().split()

a = int(valores[0])
ultimo = len(valores) - 1
n = int(valores[ultimo])

soma = 0
for i in range(n):
    soma += a + i
print(soma)
