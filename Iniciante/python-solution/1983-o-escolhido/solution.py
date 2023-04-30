x = int(input())

alunos = []
notas = []
for i in range(x):
    aluno, nota = input().split()
    alunos.append(aluno)
    notas.append(float(nota))

maior = 0
for i in range(1, len(notas)):
    if notas[i] > maior and notas[i] >= 8:
        maior = notas[i]
        x = i

if maior == 0:
    print("Minimum note not reached")
else:
    print(alunos[x])
