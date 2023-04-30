h, z, l = map(int, input().split(" "))

sobrinhos = [h, z, l]
sobrinhos.sort()

if sobrinhos[1] == z:
    print("zezinho")
elif sobrinhos[1] == l:
    print("luisinho")
else:
    print("huguinho")
