n = int(input())
valores = list(map(int, input().split()))

minimo = min(valores)
resultado = valores.index(minimo) + 1

print(resultado)