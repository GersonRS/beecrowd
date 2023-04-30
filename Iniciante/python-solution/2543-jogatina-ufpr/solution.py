while True:
    try:

        def jogatina(n, i):
            gameplay_cs = 0
            for entradas in range(n):
                id, j = map(int, input().split())
                if id == i and j == 0:
                    gameplay_cs += 1
            return gameplay_cs

        n, i = map(int, input().split())
        print(jogatina(n, i))
    except EOFError:
        break
