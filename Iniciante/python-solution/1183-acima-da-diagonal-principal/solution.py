operacao = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(12):
    for j in range(i+1, 12):
        soma += matriz[i][j]

if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = soma / 66
    print(f'{media:.1f}')