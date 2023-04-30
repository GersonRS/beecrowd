l = int(input())
t = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for a in matriz[l]:
    soma += a

if t == "S":
    print(soma)
else:
    print(soma / 12)
