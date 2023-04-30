d1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(':'))
total1 = (d1*24*60*60)+(h1*60*60)+(m1*60)+(s1)

d2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(':'))
total2 = (d2*24*60*60)+(h2*60*60)+(m2*60)+s2

dif = total2-total1
dia = dif // 86400
dif = dif % 86400

hora = dif // 3600
dif = dif % 3600

min = dif // 60
dif = dif % 60

seg = dif

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{min} minuto(s)')
print(f'{seg} segundo(s)')