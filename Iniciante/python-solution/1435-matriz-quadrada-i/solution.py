while True:
    n = int(input())
    if n == 0:
        break

    for i in range(0, n):
        for j in range(0, n):
            if i < n - i - 1:
                linha = i
            else:
                linha = n - i - 1

            if j < n - j - 1:
                coluna = j
            else:
                coluna = n - j - 1

            if coluna < linha:
                dist = coluna
            else:
                dist = linha

            print(f"{dist+1:3}", end="")
            if j != n - 1:
                print(end=" ")
        print()
    print()
