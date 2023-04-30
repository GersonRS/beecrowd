n = []

for i in range(20):
    n.append(int(input()))

n.reverse()

for j in range(20):
    print(f"N[{j}] = {n[j]}")
