soma = 0
inter = 0
gremio = 0
empate = 0

while True:
    i, g = map(int, input().split(" "))
    soma += 1
    if i == g:
        empate += 1
    elif i > g:
        inter += 1
    else:
        gremio += 1

    print("Novo grenal (1-sim 2-nao)")
    x = int(input())
    if x != 1:
        break

print(f"{soma} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
