valores = map(int, input().split())
ordem = sorted(valores)

if ordem[0]**2 + ordem[1]**2 == ordem[2]**2:
    retangulo = 'S'
else:
    retangulo = 'N'


if ordem[0] + ordem[1] > ordem[2]:
    if ordem[0] == ordem[1] and ordem[0] == ordem[2]:
        print('Valido-Equilatero')
        print(f'Retangulo: {retangulo}')
    elif ordem[0] == ordem[1] or ordem[0] == ordem[2] or ordem[1] == ordem[2]:
        print('Valido-Isoceles')
        print(f'Retangulo: {retangulo}')
    else:
        print('Valido-Escaleno')
        print(f'Retangulo: {retangulo}')

else:
    print('Invalido')