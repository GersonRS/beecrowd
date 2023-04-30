l1 = input().split()
A = float(l1[0])
B = float(l1[1])
C = float(l1[2])

areaTriangulo = A * C / 2
areaCirculo = 3.14159 * C**2
areaTrapezio = (A + B) * C / 2
areaQuadrado = B**2
areaRetangulo = A * B


print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")
