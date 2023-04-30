flag = False

while True:
    try:
        linha = input()
        if "<body>" in linha:
            flag = True
            continue
        if "</body>" in linha:
            break
        if flag:
            print(linha)
    except EOFError:
        break