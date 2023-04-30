while True:
    t = int(input())
    if t == 0:
        break

    for i in range(t):
        n = int(input())
        pedidos = 0
        if n % 2 == 0:
            pedidos = 4 * (n // 2 - 1) + 2
        else:
            pedidos = 4 * (n // 2) + 1
        print(pedidos)
