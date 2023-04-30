# a, b, c = map(int, input().split())
#
# order = sorted([a, b, c])
# if order[0] + order[1] == order[2] or a == b or b == c or c == a:
#     print('S')
# else:
#     print('N')

import math

while True:
    try:
        x1, y1, x2, y2, v, r1, r2 = map(int, input().split())
        distancia_entre_dois_pontos = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        distancia = distancia_entre_dois_pontos + v * 1.5
        raio = r1 + r2

        if distancia > raio:
            print('N')
        else:
            print('Y')
    except EOFError:
        break
