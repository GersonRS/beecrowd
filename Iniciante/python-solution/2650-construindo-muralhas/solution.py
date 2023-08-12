vezes, tamanho_muralha = map(int, input().split())
for i in range(vezes):
    entrada = input().split()
    if int(entrada[-1]) > tamanho_muralha:
        print(" ".join(entrada[0:-1]))
