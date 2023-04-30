regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"],
}
t = int(input())
for i in range(1, t + 1):
    escolhas = input().split()

    if escolhas[0] == escolhas[1]:
        reacao = "De novo!"
    else:
        if escolhas[1] in regras[escolhas[0]]:
            reacao = "Bazinga!"
        else:
            reacao = "Raj trapaceou!"

    print(f"Caso #{i}: {reacao}")
