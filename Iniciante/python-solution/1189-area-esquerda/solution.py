operacao = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

x = 0
y = 1
verde = []
for i in range(1, 11):
    for j in range(x, y):
        verde.append(matriz[i][j])
    if i < 5:
        y += 1
    if i > 5:
        y -= 1

soma = 0
media = 0
if operacao == 'S':
    soma = sum(verde)
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = sum(verde)/len(verde)
    print(f'{media:.1f}')