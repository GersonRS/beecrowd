real, cent = map(int, input().split("."))
cent = cent + real * 100

y = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for n in y:
    print(f"{cent//(n*100)} nota(s) de R$ {n}.00")
    cent = cent % (n * 100)

j = [100, 50, 25, 10, 5, 1]
print("MOEDAS:")
for m in j:
    print(f"{cent//m} moeda(s) de R$ {m/100:.2f}")
    cent = cent % m
