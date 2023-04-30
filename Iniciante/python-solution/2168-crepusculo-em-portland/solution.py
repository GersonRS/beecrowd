n = int(input())

quadras = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    linha = list(map(int, input().split()))
    for j in range(n+1):
        quadras[i][j] = linha[j]

for i in range(n):
    for j in range(n):
        if quadras[i][j] + quadras[i][j+1] + quadras[i+1][j] + quadras[i+1][j+1] < 2:
            print('U', end='')
        else:
            print('S', end='')
    print()
