n = int(input())
coelho = 0
sapo = 0
rato = 0
total = 0
for i in range(n):
    num, tipo = input().split()
    num = int(num)
    tipo = str(tipo)

    total += num

    if tipo == "C":
        coelho += num
    elif tipo == "S":
        sapo += num
    elif tipo == "R":
        rato += num

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")

print(f"Percentual de coelhos: {coelho/total*100:.2f} %")
print(f"Percentual de ratos: {rato/total*100:.2f} %")
print(f"Percentual de sapos: {sapo/total*100:.2f} %")
