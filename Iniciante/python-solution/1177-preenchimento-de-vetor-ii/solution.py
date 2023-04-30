t = int(input())

n = [0]*1000

for i in range(len(n)):
    x = i % t
    n[i] = x

for i in range(len(n)):
    print(f'N[{i}] = {n[i]}')