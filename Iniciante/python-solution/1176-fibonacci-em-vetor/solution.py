t = int(input())

vet = [0, 1]

for i in range(2, 61):
    vet.append(vet[i - 1] + vet[i - 2])

for i in range(t):
    n = int(input())
    print(f"Fib({n}) = {vet[n]}")
