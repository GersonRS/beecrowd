x = float(input())

if x >= 0 and x <= 25:
    print('Intervalo [0,25]')
elif x > 25 and x <= 50:
    print('Intervalo (25,50]')
elif x > 50 and x <= 75:
    print('Intervalo (50,75]')
elif x > 75 and x <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')