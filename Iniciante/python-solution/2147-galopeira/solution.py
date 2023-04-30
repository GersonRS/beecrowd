def galopeira(c):
    for i in range(c):
        palavra = input()
        num_palavra = len(palavra)
        resultado = num_palavra * 0.01
        print(f'{resultado:.2f}')

c = int(input())
galopeira(c)