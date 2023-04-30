n = int(input())
valores = list(map(int, input().split()))
estrelas = [0] * n
i = 0
while True:
    if i == 0 and valores[i] % 2 == 0:
        estrelas[i] = 1
        if valores[i] > 0:
            valores[i] -= 1
        break
    elif i == n-1 and valores[i] % 2 == 1:
        estrelas[i] = 1
        if valores[i] > 0:
            valores[i] -= 1
        break
    elif valores[i] % 2 == 1:
        valores[i] -= 1
        estrelas[i] = 1
        i += 1
    elif valores[i] % 2 == 0:
        estrelas[i] = 1
        if valores[i] > 0:
            valores[i] -= 1
        i -= 1

sum_valores = sum(valores)
sum_estrelas = sum(estrelas)
print(sum_estrelas, sum_valores)
