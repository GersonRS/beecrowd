while True:
    try:
        n = int(input())
        m, l = map(int, input().split())

        marcos = []
        for i in range(m):
            atributos = list(map(int, input().split()))
            marcos.append(atributos)

        leo = []
        for i in range(l):
            atributos = list(map(int, input().split()))
            leo.append(atributos)

        CM, CL = map(int, input().split())
        atributo = int(input())

        if marcos[CM - 1][atributo - 1] > leo[CL - 1][atributo - 1]:
            print('Marcos')
        elif leo[CL - 1][atributo - 1] > marcos[CM - 1][atributo - 1]:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break
