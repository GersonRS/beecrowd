x, y = list(map(int, input().split()))
cont = 1
for i in range(1, (int((y / x)) + 1)):
    r = ""
    for y in range(x):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])
