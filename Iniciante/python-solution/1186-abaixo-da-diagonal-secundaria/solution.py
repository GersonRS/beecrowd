operacao = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
cont = 0
for i in range(12):
    for j in range(12):
        if (i+j > 11):
            soma += matriz[i][j]
            cont += 1

if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    print(f'{soma/cont:.1f}')
