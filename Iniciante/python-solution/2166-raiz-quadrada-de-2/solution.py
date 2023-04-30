n = int(input())
x = 0.0
while n > 0:
    x += 2.0
    x = 1.0 / x
    n -= 1
x += 1.0
print(f'{x:.10f}')
