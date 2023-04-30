def sweeper(matriz, i, j):
    p = 0
    l = len(matriz) - 1
    c = len(matriz[i]) - 1
    if i > 0 and matriz[i - 1][j] == 1:
        p += 1
    if i < l and matriz[i + 1][j] == 1:
        p += 1
    if j > 0 and matriz[i][j - 1] == 1:
        p += 1
    if j < c and matriz[i][j + 1] == 1:
        p += 1
    return p


while True:
    try:
        n, m = map(int, input().split())
        matriz = [list(map(int, input().split())) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matriz[i][j] == 1:
                    print("9", end="")
                else:
                    print(sweeper(matriz, i, j), end="")
            print()
    except EOFError:
        break
