n = int(input())
for i in range(n):
    h, m, o = map(int, input().split())
    if h < 10 or m < 10:
        h, m = h + 00, m + 00

    if o == 1:
        ocorrencia = "A porta abriu!"
    else:
        ocorrencia = "A porta fechou!"
    print(f"{h:02d}:{m:02d} - {ocorrencia}")
