n = int(input())

for i in range(n):
    jogadores = input().split(' ')
    jogada1, jogada2 = map(int, input().split(' '))
    soma = jogada1 + jogada2

    if soma % 2 == 0 and jogadores[1] == 'PAR' or soma % 2 != 0 and jogadores[1] == 'IMPAR':
        print(f'{jogadores[0]}')
    else:
        print(f'{jogadores[2]}')