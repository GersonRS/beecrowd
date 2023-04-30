while True:
    try:

        def montanha_russa(n, a_minima, a_maxima):
            alturas = [0] * n
            for i in range(len(alturas)):
                x = int(input())
                alturas[i] = x

            visitantes = 0
            for altura in alturas:
                if altura in range(a_minima, a_maxima + 1):
                    visitantes += 1

            return visitantes

        n, a_minima, a_maxima = map(int, input().split())
        print(montanha_russa(n, a_minima, a_maxima))

    except EOFError:
        break
