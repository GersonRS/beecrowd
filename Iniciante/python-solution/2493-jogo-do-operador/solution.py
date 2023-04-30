while True:
    try:
        t = int(input())
        expressao = []
        for i in range(t):
            entrada = input().split("=")
            expressao.append(entrada[0].split() + [entrada[1]])

        respostas = []
        for i in range(t):
            nome, escolha, resposta = input().split()
            respostas.append((nome, int(escolha), resposta))

        nao_passaram = []
        for compara in respostas:
            nome, escolha, resposta = compara

            x = int(expressao[escolha - 1][0])
            y = int(expressao[escolha - 1][1])
            z = int(expressao[escolha - 1][2])
            if resposta == "+":
                if x + y != z:
                    nao_passaram.append(nome)
            elif resposta == "-":
                if x - y != z:
                    nao_passaram.append(nome)
            elif resposta == "*":
                if x * y != z:
                    nao_passaram.append(nome)
            else:
                if x + y == z or x - y == z or x * y == z:
                    nao_passaram.append(nome)

        if len(nao_passaram) == 0:
            print("You Shall All Pass!")
        elif len(nao_passaram) == len(expressao):
            print("None Shall Pass!")
        else:
            nao_passaram.sort()
            print(" ".join(nao_passaram))

    except EOFError:
        break
