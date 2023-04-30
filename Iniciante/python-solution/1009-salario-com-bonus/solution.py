nome = input()
fixo = float(input())
vendas = float(input())

comissao = vendas * 15 / 100
salario = fixo + comissao

print(f"TOTAL = R$ {salario:.2f}")
