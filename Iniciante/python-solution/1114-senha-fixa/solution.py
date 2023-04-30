while True:
    try:
        senha = int(input())
        if senha == 2002:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except EOFError:
        break
