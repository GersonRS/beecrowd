t = int(input())

for i in range(t):
    bonus = int(input())
    bonus_dabriel = 0
    bonus_guarte = 0
    ataque1, defesa1, level1 = map(int, input().split())
    ataque2, defesa2, level2 = map(int, input().split())
    if level1 % 2 == 0:
        bonus_dabriel = bonus
    if level2 % 2 == 0:
        bonus_guarte = bonus

    valor_golpe_dabriel = ((ataque1 + defesa1) / 2) + bonus_dabriel
    valor_golpe_guarte = ((ataque2 + defesa2) / 2) + bonus_guarte

    if valor_golpe_dabriel > valor_golpe_guarte:
        print('Dabriel')
    elif valor_golpe_guarte > valor_golpe_dabriel:
        print('Guarte')
    else:
        print('Empate')


