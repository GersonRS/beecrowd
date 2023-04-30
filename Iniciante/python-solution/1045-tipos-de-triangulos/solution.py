maior = list(map(float, input().split()))
ordem = sorted(maior, reverse=True)
a, b, c = ordem

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")

elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b != c or a == c != c or c == b != a:
        print("TRIANGULO ISOSCELES")

elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b != c or a == c != c or c == b != a:
        print("TRIANGULO ISOSCELES")
