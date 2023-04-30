def decifrando(c):
    return c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == ' ' \
           or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' \
           or c == '!' or c == '@' or c == '#' or c == '$' or c == '%' \
           or c == '|' or c == '&' or c == '*' or c == '(' or c == ')' \
           or c == '.' or c == ',' or c == ';' or c == ':' or c == '?'

while True:
    try:
        line = input().strip()
        if line == "":
            continue

        C, N = map(int, line.split(" "))
        entrada1 = input().strip()
        entrada2 = input().strip()
        criptografia = [[' ' for _ in range(C + 5000)] for _ in range(4)]
        frase = ['' for _ in range(C + 5000)]

        for i in range(N):
            frase[i] = input().strip()

        for i in range(C):
            c = entrada1[i]
            d = entrada2[i]
            criptografia[0][i] = c
            criptografia[1][i] = d
            criptografia[2][i] = c.lower()
            criptografia[3][i] = d.lower()

        for i in range(N):
            msg = ""
            for c in frase[i]:
                for j in range(C):
                    if c == criptografia[0][j]:
                        msg += criptografia[1][j].lower() if decifrando(c) else criptografia[1][j]
                        break
                    elif c == criptografia[1][j]:
                        msg += criptografia[0][j].lower() if decifrando(c) else criptografia[0][j]
                        break
                    elif c == criptografia[2][j]:
                        msg += criptografia[3][j].lower() if decifrando(c) else criptografia[3][j]
                        break
                    elif c == criptografia[3][j]:
                        msg += criptografia[2][j].lower() if decifrando(c) else criptografia[2][j]
                        break
                    elif j + 1 == C:
                        msg += c
            print(msg)

        print()

    except EOFError:
        break

