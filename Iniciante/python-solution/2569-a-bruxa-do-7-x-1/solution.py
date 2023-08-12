a, op, b = input().replace("7", "0").split()
print(
    int(str(int(a) + int(b)).replace("7", "0"))
    if op == "+"
    else int(str(int(a) * int(b)).replace("7", "0"))
)
