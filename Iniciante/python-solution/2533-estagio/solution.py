while True:
    try:
        x = int(input())
        carga = 0
        nota = 0

        for i in range(x):
            m1, m2 = map(int, input().split())
            carga += m2
            nota += m1 * m2

            ira = nota / (carga * 100)
        print(f"{ira:.4f}")
    except EOFError:
        break
