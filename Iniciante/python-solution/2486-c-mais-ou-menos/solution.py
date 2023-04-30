vitamina = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34,
}
while True:
    t = int(input())
    if t == 0:
        break
    quantidade = 0
    for i in range(t):
        n, alimento = input().split(maxsplit=1)
        x = vitamina[alimento]
        quantidade += int(n) * x
    if quantidade in range(110, 131):
        print(f'{quantidade} mg')
    else:
        if quantidade < 110:
            quantidade = 110 - quantidade
            print(f'Mais {quantidade} mg')
        else:
            quantidade -= 130
            print(f'Menos {quantidade} mg')