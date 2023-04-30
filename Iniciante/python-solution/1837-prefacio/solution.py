a, b = map(int, input().split(" "))

resto = a % b
quociente = a // b
if resto < 0:
    resto += abs(b)
    quociente = -(-a // b)

print(quociente, resto)
