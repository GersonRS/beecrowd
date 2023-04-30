soma = 0
for i in range(2):
    x = float(input())
    while x < 0 or x > 10:
        print("nota invalida")
        x = float(input())

    soma += x
print(f"media = {soma / 2:.2f}")
