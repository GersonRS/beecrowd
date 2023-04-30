def pulo_sapo():
    for i in range(len(altura_canos)-1):
        diferenca = abs(altura_canos[i] - altura_canos[i+1])
        if diferenca > altura:
            return 'GAME OVER'
    return 'YOU WIN'


altura, canos = map(int, input().split())
altura_canos = list(map(int, input().split()))

print(pulo_sapo())