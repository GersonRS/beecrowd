terreno = list(map(int, input().split()))
tam_terreno = [[0 for j in range(terreno[1])] for i in range(terreno[0])]
for i in range(terreno[0]):
    linha = list(map(int, input().split()))
    for j in range(terreno[1]):
        tam_terreno[i][j] = linha[j]

sabre = False
for i in range(1, terreno[0] - 1):
    for j in range(1, terreno[1] - 1):
        if tam_terreno[i][j] == 42:
            if (
                tam_terreno[i - 1][j - 1] == 7
                and tam_terreno[i - 1][j] == 7
                and tam_terreno[i - 1][j + 1] == 7
            ):
                if tam_terreno[i][j - 1] == 7 and tam_terreno[i][j + 1] == 7:
                    if (
                        tam_terreno[i + 1][j - 1] == 7
                        and tam_terreno[i + 1][j] == 7
                        and tam_terreno[i + 1][j + 1] == 7
                    ):
                        print(i + 1, j + 1)
                        sabre = True
                        break
if sabre == False:
    print("0 0")
