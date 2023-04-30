while True:
    soma = 0
    for i in range(2):
        x = float(input())
        while x > 10 or x < 0:
            print("nota invalida")
            x = float(input())
        soma += x
    print(f"media = {soma/2:.2f}")

    while True:
        print("novo calculo (1-sim 2-nao)")
        y = int(input())
        if y == 1 or y == 2:
            break
    if y == 2:
        break
