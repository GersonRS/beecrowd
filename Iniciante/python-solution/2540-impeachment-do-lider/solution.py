while True:
    try:
        n = int(input())

        votos = [0] * n
        casos = list(map(int, input().split()))

        for i in range(n):
            votos[i] = casos[i]

        impeachment = 0
        for i in votos:
            if i == 1:
                impeachment += 1

        resultado = (n * 2) / 3

        if impeachment >= resultado:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
