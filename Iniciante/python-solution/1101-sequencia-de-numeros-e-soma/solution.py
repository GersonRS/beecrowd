while True:
    valores = [int(x) for x in input().split()]
    m = min(valores)
    n = max(valores)

    if m <= 0:
        break

    soma = 0
    for i in range(m, n + 1):
        print(i, end=" ")
        soma += i
    print(f"Sum={soma}")
