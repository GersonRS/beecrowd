def duas_notas(compra, pagamento):
    notas = [100, 50, 20, 10, 5, 2]
    troco = pagamento - compra
    for i in range(len(notas)):
        for j in range(i, len(notas)):
            if notas[i] + notas[j] == troco:
                return "possible"
    return "impossible"


while True:
    compra, pagamento = map(int, input().split())
    if compra == 0 and pagamento == 0:
        break
    print(duas_notas(compra, pagamento))
