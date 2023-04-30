while True:
    n = int(input())
    if n == 0:
        break

    resul = []
    for i in range(1, n + 1):
        matriz = []
        count = i
        for j in range(n):
            matriz.append(abs(count))
            if count == 1:
                count -= 3
            else:
                count -= 1
        resul.append(matriz)

    for i in range(n):
        x = ""
        for j in range(n):
            x += f" {resul[i][j]:3}"
        print(x[1:])
    print("")
