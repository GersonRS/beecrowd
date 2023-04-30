par = [0] * 5
impar = [0] * 5
cont_par = 0
cont_impar = 0

for i in range(15):
    x = int(input())
    if x % 2 == 0:
        par[cont_par] = x
        cont_par += 1
    else:
        impar[cont_impar] = x
        cont_impar += 1
    if cont_impar == 5:
        for j in range(5):
            print(f'impar[{j}] = {impar[j]}')
        cont_impar = 0
    if cont_par == 5:
        for j in range(5):
            print(f'par[{j}] = {par[j]}')
        cont_par = 0

for j in range(cont_impar):
    print(f'impar[{j}] = {impar[j]}')

for j in range(cont_par):
    print(f'par[{j}] = {par[j]}')