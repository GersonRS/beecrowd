b = int(input())
g = int(input())

if g % 2 != 0:
    g += -1

resto = (g // 2) - b

if resto <= 0:
    print("Amelia tem todas bolinhas!")
else:
    print(f"Faltam {resto} bolinha(s)")
