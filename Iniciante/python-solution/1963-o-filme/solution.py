antigo, novo = map(float, input().split())

porcentagem = (novo/antigo*100)-100

print(f'{porcentagem:.2f}%')