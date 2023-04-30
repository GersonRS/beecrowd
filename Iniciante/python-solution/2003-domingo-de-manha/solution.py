n = int(input())

for i in range(n):
    jogador_1 = input()
    jogador_2 = input()
    if jogador_2 == "pedra":
        if jogador_1 == "pedra":
            print("Sem ganhador")
        elif jogador_1 == "papel":
            print("Jogador 2 venceu")
        else:
            print("Jogador 1 venceu")

    elif jogador_2 == "papel":
        if jogador_1 == "papel":
            print("Ambos venceram")
        elif jogador_1 == "pedra":
            print("Jogador 1 venceu")
        else:
            print("Jogador 1 venceu")

    elif jogador_2 == "ataque":
        if jogador_1 == "ataque":
            print("Aniquilacao mutua")
        elif jogador_1 == "pedra":
            print("Jogador 2 venceu")
        else:
            print("Jogador 2 venceu")
