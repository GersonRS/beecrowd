operacao = input()

matriz= []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
    
soma = 0  
x = 12
cont = 0
for i in range(11):
    x -= 1
    for j in range(x):
        soma += matriz[i][j]
        cont += 1
        
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = soma / cont
    print(f'{media:.1f}')