a, b, c = map(int, input().split(' '))

if a > b:
    if b <= c:
        print(':)')
    elif (a - b) > (b - c):
        print(':)')
    else:
        print(':(')
elif a < b:
    if b >= c:
        print(':(')
    elif (a - b) < (b - c):
        print(':(')
    else:
        print(':)')
else:
    if b < c:
        print(':)')
    else:
        print(':(')
