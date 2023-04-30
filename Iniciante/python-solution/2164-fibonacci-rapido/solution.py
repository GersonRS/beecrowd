import math
n = int(input())

fibo = ((math.pow((1+math.sqrt(5))/2.0, n)) - (math.pow((1-math.sqrt(5))/2.0, n))) / math.sqrt(5)

print(f'{fibo:.1f}')