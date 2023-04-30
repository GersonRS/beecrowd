def raiz(n):
    x = 0.0

    while n:
        x += 6.0
        x = 1.0 / x
        n -= 1

    x += 3.0
    print(f"{x:.10f}")


n = int(input())
raiz(n)
