A, B, C = map(int, input().split())

maiorAB = (A + B + abs(A - B)) / 2
maiorC = (maiorAB + C + abs(maiorAB - C)) / 2

print(f"{maiorC:.0f} eh o maior")
