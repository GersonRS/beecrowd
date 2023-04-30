s = input()

cont = 0
for i in s:
    if i == '1':
        cont += 1

if cont % 2 == 0:
    print(f'{s}0')
else:
    print(f'{s}1')