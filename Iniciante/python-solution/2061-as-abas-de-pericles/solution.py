def abas_restante(abas, operacao):
    fechou = 0
    clicou = 0
    for i in range(operacao):
        acao = input()
        if acao == "fechou":
            fechou += 1
        else:
            clicou += 1
    abas += fechou - clicou

    return abas


abas, operacao = map(int, input().split())
print(abas_restante(abas, operacao))
