n = int(input())
for j in range(n):
    x, y = map(int, input().split(" "))
    if x % 2 == 0:
        x += 1

    soma = 0
    for i in range(0, y):
        soma += x
        x += 2
    print(soma)
