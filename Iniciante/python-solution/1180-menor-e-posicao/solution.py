n = int(input())
x = list(map(int, input().split()))
print(f"Menor valor: {min(x)}")
print(f"Posicao: {x.index(min(x))}")
