n = int(input())
medidas = [0] * n
rotacoes = list(map(int, input().split()))

for i in range(n):
    medidas[i] = rotacoes[i]

resultado = None
for i in range(n - 1):
    if medidas[i] > medidas[i + 1]:
        resultado = i + 2
        print(resultado)
        break
if resultado == None:
    print("0")
