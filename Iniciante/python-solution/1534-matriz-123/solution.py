while True:
    try:
        n = int(input())

        matriz = []
        for i in range(0, n):
            matriz.append([])
            for j in range(0, n):
                matriz[i].append('3')

            c1 = n - 1

        for i in range(0, n):
            matriz[i][i] = '1'
            matriz[i][c1] = '2'
            c1 -= 1
            resul = ''.join(matriz[i])
            print(resul)
    except EOFError:
        break