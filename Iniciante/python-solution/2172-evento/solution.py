while True:
    x, m = map(int, input().split())

    if x == 0 and m == 0:
        break
    resultado = x * m
    print(resultado)
