n = int(input())

grupos = {'bonecos':0, 'arquitetos':0, 'musicos':0, 'desenhistas':0}
for i in range(n):
    linha = input().split()
    grupo = linha[1]
    horas = int(linha[2])
    grupos[grupo] += horas

p = sum(grupos[grupo] // grupo_horas for grupo, grupo_horas in {"bonecos":8, "arquitetos":4, "musicos":6, "desenhistas":12}.items())
print(p)