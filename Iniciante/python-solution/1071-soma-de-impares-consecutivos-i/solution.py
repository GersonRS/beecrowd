x = int(input())
y = int(input())

soma = 0
for i in range(y + 1, x):
    if i % 2 != 0:
        soma += i
print(soma)