while True:
    try:
        x = input()
        letras = list(x)
        n = int(input())
        entrada = list(map(lambda x: int(x) - 1, input().split()))
        for i in range(len(entrada)):
            if i == len(entrada) - 1:
                print(letras[entrada[i]])
            else:
                print(letras[entrada[i]], end="")

    except EOFError:
        break
