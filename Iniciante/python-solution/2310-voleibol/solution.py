soma_s = 0
soma_b = 0
soma_a = 0
soma_s1 = 0
soma_b1 = 0
soma_a1 = 0

n = int(input())
for i in range(n):
    nome = input()
    s, b, a = map(int, input().split())
    s1, b1, a1 = map(int, input().split())
    soma_s += s
    soma_b += b
    soma_a += a
    soma_s1 += s1
    soma_b1 += b1
    soma_a1 += a1

saque = soma_s1 / soma_s * 100
bloqueio = soma_b1 / soma_b * 100
ataque = soma_a1 / soma_a * 100
print(f"Pontos de Saque: {saque:.2f} %.")
print(f"Pontos de Bloqueio: {bloqueio:.2f} %.")
print(f"Pontos de Ataque: {ataque:.2f} %.")
