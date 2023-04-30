x = float(input())

vet = [0]*100

for i in range(100):
    vet[i] = x
    x /= 2

for i in range(100):
    print(f'N[{i}] = {vet[i]:.4f}')
