n = int(input())
min_classificados = int(input())

competidores = [int(input()) for i in range(n)]
competidores = sorted(competidores, reverse=True) + [0]

i = min_classificados
while i < n and competidores[i] == competidores[min_classificados - 1]:
    i += 1

print(i)
