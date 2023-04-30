x = int(input())
y = int(input())
if x > y:
    x, y = y, x

soma = 0
for i in range(x, y+1):
    if i % 13 != 0:
        soma += i
print(soma)