caso = 1

while True:
    try:
        n = int(input())

        seq = [0]
        total = 0
        for i in range(n + 1):
            seq += [i] * i
            total += i
        if total + 1 == 1:
            print(f"Caso {caso}: {total + 1} numero")
            print(" ".join(map(str, seq)))
            print()
        else:
            print(f"Caso {caso}: {total + 1} numeros")
            print(" ".join(map(str, seq)))
            print()

        caso += 1

    except EOFError:
        break
