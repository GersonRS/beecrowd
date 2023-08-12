a, b, c = map(float, input().split(" "))
if a == 0:
    print("Impossivel calcular")
else:
    delta = b * b + (-4 * a * c)
    if delta < 0:
        print("Impossivel calcular")
    else:
        import math
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")
