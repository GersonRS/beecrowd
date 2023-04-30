x = int(input())
soma = x
cont = 1
while x >= 0:
    x = int(input())
    if x >= 0:
        soma += x
        cont += 1
media = soma/cont
print(f'{media:.2f}')