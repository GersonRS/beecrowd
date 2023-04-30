while True:
    try:
        n, m = map(int, input().split())
        cidade = []
        for i in range(n):
            linha = list(map(int, input().split()))
            cidade.append(linha)

        for i in range(n):
            for j in range(m):
                if cidade[i][j] == 1:
                    linha_eu = i
                    coluna_eu = j
                elif cidade[i][j] == 2:
                    linha_analogimon = i
                    coluna_analogimon = j
        
        distancia_minima = abs(linha_eu - linha_analogimon) + abs(coluna_eu - coluna_analogimon)
        print(distancia_minima)

    except EOFError:
        break