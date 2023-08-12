movs = [
    "tesoura",
    "papel",
    "pedra",
    "lagarto",
    "spock",
    "tesoura",
    "lagarto",
    "papel",
    "spock",
    "pedra",
    "tesoura",
]

n = int(input())

for _ in range(n):
    rajesh, sheldon = input().split()

    vitoria = "empate"
    for i in range(len(movs) - 1):
        if movs[i] == rajesh and movs[i + 1] == sheldon:
            vitoria = "rajesh"
        elif movs[i] == sheldon and movs[i + 1] == rajesh:
            vitoria = "sheldon"
    print(vitoria)
