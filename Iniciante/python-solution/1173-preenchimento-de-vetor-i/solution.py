n = int(input())

x = [0]*10

for i in range(len(x)):
    x[i] = n
    n *= 2
    print(f'N[{i}] = {x[i]}')