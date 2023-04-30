def senha():
    while True:
        try:
            n = int(input())
            senha = n - 1
            print(senha)
        except EOFError:
            break
senha()