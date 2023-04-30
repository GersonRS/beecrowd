n = 0
pos = 0
for i in range(1, 101):
    x = int(input())
    if x > n:
        n = x
        pos = i
print(n)
print(pos)
