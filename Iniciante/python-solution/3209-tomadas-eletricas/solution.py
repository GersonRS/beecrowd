n = int(input())

for i in range(n):
    linha = list(map(int, input().split()))

    k = linha[0]
    o = linha[1:]

    soma = sum(o)
    resul = soma - k + 1

    print(resul)
