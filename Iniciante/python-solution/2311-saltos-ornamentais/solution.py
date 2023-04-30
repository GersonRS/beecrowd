n = int(input())
for i in range(n):
    nome = input()
    gd = float(input())
    valores = map(float, input().split())
    ordem = sorted(valores)[1:-1]
    nota = gd * sum(ordem)
    print(f'{nome} {nota:.2f}')