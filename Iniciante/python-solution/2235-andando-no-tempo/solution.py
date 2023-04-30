def andando_no_tempo():
    a, b, c = map(int, input().split())

    order = sorted([a, b, c])
    if order[0] + order[1] == order[2] or a == b or b == c or c == a:
        print('S')
    else:
        print('N')

andando_no_tempo()
