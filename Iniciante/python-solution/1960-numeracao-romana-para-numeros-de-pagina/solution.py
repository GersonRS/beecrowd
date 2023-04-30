def converter_para_romano(numero):
    letras_romanas = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90),
                      ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
    romano = ""
    for letra, valor in letras_romanas:
        while numero >= valor:
            romano += letra
            numero -= valor
    return romano

numero = int(input())
print(converter_para_romano(numero))

