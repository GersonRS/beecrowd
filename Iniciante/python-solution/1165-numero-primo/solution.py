n = int(input())

for i in range(n):
    x = int(input())
    primo = 0
    for j in range(1, x + 1):
        if x % j == 0:
            primo += 1
    if primo == 2:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
