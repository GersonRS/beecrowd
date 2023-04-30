n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    x1 = min(x, y)
    y1 = max(x, y)

    soma = 0
    for j in range(x1 + 1, y1):
        if j % 2 != 0:
            soma += j
    print(soma)
