x = float(input())

imposto = 0
if x <= 2000:
    print('Isento')
elif x <= 3000:
    imposto = (x-2000)*0.08
    print(f'R$ {imposto:.2f}')
elif x <= 4500:
    imposto = (1000 * 0.08)+((x - 3000) * 0.18)
    print(f'R$ {imposto:.2f}')
else:
    imposto = (1000 * 0.08)+(1500 * 0.18)+((x - 4500) * 0.28)
    print(f'R$ {imposto:.2f}')