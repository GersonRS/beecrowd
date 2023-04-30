t = int(input())
for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    pa = int(pa)
    pb = int(pb)

    anos = 0
    while pa <= pb:
        pa = int(pa + (pa * g1 / 100))
        pb = int(pb + (pb * g2 / 100))
        anos += 1
        if anos > 100:
            print("Mais de 1 seculo.")
            break

    if anos <= 100:
        print(f"{anos} anos.")
