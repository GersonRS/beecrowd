import math
while True:
    x = input()
    if x == '0':
        break
    a, b, c = x.split(' ')

    metro = (int(a) * int(b) * 100) / int(c)
    lado = math.sqrt(metro)
    print(int(lado))