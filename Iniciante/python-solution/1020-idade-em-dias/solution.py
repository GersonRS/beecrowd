y = int(input())
ano = y // 365
resto = y % 365
mes = resto // 30
dia = resto % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
