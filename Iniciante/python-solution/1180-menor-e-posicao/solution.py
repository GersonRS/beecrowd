n = int(input())
x = input().split()
x = list(map(int, (x)))

menor = x[0]
posi = 0
for i in range(1, n):
    if x[i] < menor:
        menor = x[i]
        posi = i

print(f"Menor valor: {menor}")
print(f"Posicao: {posi}")
