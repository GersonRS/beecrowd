caso = 1
while True:
    try:
        q1 = input()
        q2 = input()
        pos = q2.count(q1)
        print(f'Caso #{caso}:')
        if pos == 0:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: {pos}')
            pos = q2.rfind(q1)
            pos = int(pos) + 1
            print(f'Pos: {pos}')
        caso += 1
        print()
    except EOFError:
        break