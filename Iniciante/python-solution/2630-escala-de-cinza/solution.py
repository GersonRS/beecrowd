def maximo(r, g, b):
    maior = sorted([r, g, b])
    return maior[2]

def minimo(r, g, b):
    menor = sorted([r, g, b])
    return menor[0]

def mean(r, g, b):
    media = (r + g + b) / 3
    return int(media)

def eye(r, g, b):
    p = (r*0.3) + (g*0.59) + (b*0.11)
    return int(p)

t = int(input())

for i in range(1, t+1):
    escala = input()
    r, g, b = map(int, input().split())
    if escala == 'max':
        print(f'Caso #{i}: {maximo(r, g, b)}')
    elif escala == 'min':
        print(f'Caso #{i}: {minimo(r, g, b)}')
    elif escala == 'mean':
        print(f'Caso #{i}: {mean(r, g, b)}')
    else:
        print(f'Caso #{i}: {eye(r, g, b)}')

