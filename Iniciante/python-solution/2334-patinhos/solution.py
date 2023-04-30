while True:
    patos = int(input())
    if patos < 0:
        break
    else:
        if patos == 0:
            print('0')
        else:
            patos -= 1
            print(patos)