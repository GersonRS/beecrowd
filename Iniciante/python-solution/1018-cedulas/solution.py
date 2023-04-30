x = int(input())

print(x)
y = [100, 50, 20, 10, 5, 2, 1]

for i in y:
    quant = x // i
    print(f"{quant} nota(s) de R$ {i},00")
    x -= quant * i
