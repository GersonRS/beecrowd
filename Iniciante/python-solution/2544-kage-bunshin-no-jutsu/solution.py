import math

while True:
    try:

        def jutsu_clones(n):
            clones = int(math.log(n, 2))
            return clones

        n = int(input())
        print(jutsu_clones(n))

    except EOFError:
        break
