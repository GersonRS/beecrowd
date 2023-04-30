def muito_tempo(n):
    for i in range(n):
        x = int(input())
        if x > 2014:
            a = abs(x - 2014)
            print(f'{a} A.C.')
        else:
            a = abs(x - 2015)
            print(f'{a} D.C.')

n = int(input())
muito_tempo(n)