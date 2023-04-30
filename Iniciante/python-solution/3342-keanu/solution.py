n = int(input())

resul = n * n
resul = resul // 2

if n % 2 != 0:
    print(f'{resul+1} casas brancas e {resul} casas pretas')
else:
    print(f'{resul} casas brancas e {resul} casas pretas')