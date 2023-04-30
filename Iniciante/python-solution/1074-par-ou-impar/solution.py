n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:
        print("NULL")
    elif x % 2 != 0 and x > 0:
        print("ODD POSITIVE")
    elif x % 2 != 0 and x < 0:
        print("ODD NEGATIVE")
    elif x % 2 == 0 and x > 0:
        print("EVEN POSITIVE")
    else:
        print("EVEN NEGATIVE")
