notas = {
    0: "E",
    range(1, 36): "D",
    range(36, 61): "C",
    range(61, 86): "B",
    range(86, 101): "A",
}


def verificar(n):
    for faixa, letra in notas.items():
        if isinstance(faixa, int):
            if n == faixa:
                return letra
        else:
            if n in faixa:
                return letra


n = int(input())
verificado = verificar(n)
print(verificado)
