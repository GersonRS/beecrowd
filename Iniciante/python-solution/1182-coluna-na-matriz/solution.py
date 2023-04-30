coluna = int(input())
t = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for a in range(12):
    soma += matriz[a][coluna]

if t == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')