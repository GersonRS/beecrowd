code1, qtd1, valor1 = list(map(float, input().split()))
code2, qtd2, valor2 = list(map(float, input().split()))

valor = qtd1 * valor1 + qtd2 * valor2

print(f"VALOR A PAGAR: R$ {valor:.2f}")
