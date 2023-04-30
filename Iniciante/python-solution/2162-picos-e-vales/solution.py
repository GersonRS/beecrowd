n = int(input())
valores = list(map(int, input().split()))

resultado = 1
for i, valor in enumerate(valores[:-1]):
    if valor == valores[i+1]:
        resultado = 0
    elif i < len(valores)-2 and valor > valores[i+1] and valores[i+1] > valores[i+2]:
        resultado = 0
    elif i < len(valores)-2 and valor < valores[i+1] and valores[i+1] < valores[i+2]:
        resultado = 0

print(resultado)

