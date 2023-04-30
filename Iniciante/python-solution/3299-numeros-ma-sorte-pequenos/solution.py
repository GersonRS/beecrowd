n = int(input())

caractere = str(n)

for i in range(len(caractere)-1):
    if caractere[i] == '1' and caractere[i+1] == '3':
        print(f'{n} es de Mala Suerte')
        break
else:
    print(f'{n} NO es de Mala Suerte')
