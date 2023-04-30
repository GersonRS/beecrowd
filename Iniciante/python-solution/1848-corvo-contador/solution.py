soma1 = soma2 = soma3 = 0

for i in range(3):
    soma_parcial = 0
    while True:
        entrada = input().strip()
        if entrada == "caw caw":
            if i == 0:
                soma1 = soma_parcial
            elif i == 1:
                soma2 = soma_parcial
            else:
                soma3 = soma_parcial
            break
        else:
            soma_parcial += int(entrada.replace("-", "0").replace("*", "1"), 2)

print(soma1)
print(soma2)
print(soma3)
