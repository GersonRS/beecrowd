pi = 3.14
while True:
    try:
        v = float(input())
        d = float(input())
        raio = d / 2
        area = pi * (raio*raio)
        altura = v / area

        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')

    except EOFError:
        break