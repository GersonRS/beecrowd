i, f = map(int, input().split())
if i < f:
    soma = f - i
else:
    soma = (24 - i) + f
print(f"O JOGO DUROU {soma} HORA(S)")
