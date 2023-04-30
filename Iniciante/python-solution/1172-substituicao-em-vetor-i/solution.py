x = []
for i in range(10):
    valor = int(input())
    x.append(valor)
    if x[i] <= 0:
        x[i] = 1
    print(f'X[{i}] = {x[i]}')