while True:
    try:
        n = int(input())
        treinos = []
        for i in range(n):
            t, d = map(int, input().split())
            treinos.append((t, d))

        recordes = [1]
        recorde_atual = treinos[0][1] / treinos[0][0]
        for i in range(1, n):
            velocidade_media = treinos[i][1] / treinos[i][0]
            if velocidade_media > recorde_atual:
                recorde_atual = velocidade_media
                recordes.append(i + 1)

        for recorde in recordes:
            print(recorde)
    except EOFError:
        break
