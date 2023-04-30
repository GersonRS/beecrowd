def exame_geral(notas, posicao):
    return notas[posicao - 1]

while True:
    try:
        n, q = map(int, input().split())

        notas = []
        for i in range(n):
            notas.append(int(input()))

        notas_ordenadas = sorted(notas, reverse=True)

        for i in range(q):
            posicao = int(input())
            nota = exame_geral(notas_ordenadas, posicao)
            print(nota)

    except EOFError:
        break
