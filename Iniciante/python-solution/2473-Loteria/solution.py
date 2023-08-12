resposta = ["terno", "quadra", "quina", "sena"]

aposta = input().split()
resultado = input().split()

aposta.extend(resultado)

c = set(aposta)
acertos = 12 - len(c)

if acertos >= 3:
    print(resposta[acertos - 3])
else:
    print("azar")
