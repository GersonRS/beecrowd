while True:
    try:
        n = int(input())
    except EOFError:
        break

    matriz = []
    for i in range(n):
        linha = [0] * n
        matriz.append(linha)

    for i in range(n):
        matriz[i][i] = 2

    for i in range(n):
        matriz[i][n - i - 1] = 3

    for i in range(n // 3, n - n // 3):
        for j in range(n // 3, n - n // 3):
            matriz[i][j] = 1

    if n % 2 == 1:
        matriz[n // 2][n // 2] = 4

    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end="")
        print()
    print()
