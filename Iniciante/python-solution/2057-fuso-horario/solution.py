s, t, f = map(int, input().split())

soma = s + t + f
if soma >= 24:
    soma -= 24
elif soma < 0:
    soma = 24 + soma
elif soma == 24:
    soma = 0

print(soma)