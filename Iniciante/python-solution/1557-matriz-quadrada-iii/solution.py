while True:
    n = int(input())
    if n == 0:
        break
    
    # Encontrando o número de dígitos do maior número da matriz
    maior_num = 2 ** (2 * (n-1))
    num_digitos = len(str(maior_num))
    
    # Construindo a matriz
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(str(2**(i+j)).rjust(num_digitos))
        matriz.append(linha)
    
    # Imprimindo a matriz formatada
    for linha in matriz:
        print(' '.join(linha))
    print()
