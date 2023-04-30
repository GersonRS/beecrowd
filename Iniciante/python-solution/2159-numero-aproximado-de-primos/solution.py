import math
n = int(input())

p = n / (math.log(n))
m = 1.25506 * n / (math.log(n))

print(f'{p:.1f} {m:.1f}')