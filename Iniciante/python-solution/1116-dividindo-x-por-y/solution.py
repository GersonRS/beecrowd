n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    else:
        div = x/y
        print(f'{div:.1f}')