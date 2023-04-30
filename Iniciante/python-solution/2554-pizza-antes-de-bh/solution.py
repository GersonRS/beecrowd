while True:
    try:
        def pizza(n, d):
            resultado = []
            for i in range(d):
                entrada = list(input().split())
                data = entrada[0]
                pessoas = [int(x) for x in entrada[1:]]
                soma = sum(pessoas)
                if soma == n:
                    resultado.append((soma, data))

            if resultado:
                return resultado[0][1]
            else:
                return 'Pizza antes de FdI'

        n, d = map(int, input().split())
        print(pizza(n, d))
    except EOFError:
        break
