cardapio = {
    '1001': 1.50,

    '1002': 2.50,

    '1003': 3.50,

    '1004': 4.50,

    '1005': 5.50,
}

produtos = int(input())
soma = 0
for i in range(produtos):
    id, quantidade = input().split()
    soma += cardapio[id] * int(quantidade)

print(f'{soma:.2f}')
