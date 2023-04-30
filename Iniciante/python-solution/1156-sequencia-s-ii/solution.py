s = 0
y = 1
for i in range(1, 40, 2):
    s += i / y
    y *= 2

print(f'{s:.2f}')