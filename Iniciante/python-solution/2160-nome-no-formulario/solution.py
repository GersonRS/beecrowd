def formulario(l):
    tamanho = len(l)

    if tamanho <= 80:
        return "YES"
    else:
        return "NO"


l = input()
x = formulario(l)
print(x)
