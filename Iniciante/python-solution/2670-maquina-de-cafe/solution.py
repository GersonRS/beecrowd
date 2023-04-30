a = int(input())
b = int(input())
c = int(input())

a1 = (a*2+b)*2
a2 = (a+c)*2
a3 = (b+c*2)*2

menor = sorted([a1, a2, a3])
print(menor[0])