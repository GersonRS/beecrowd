while True:
    try:
        n = int(input())
        velocidade = map(int, input().split())

        max_speed = max(velocidade)

        if max_speed < 10:
            nivel = 1
        elif max_speed < 20:
            nivel = 2
        else:
            nivel = 3

        print(nivel)

    except EOFError:
        break
