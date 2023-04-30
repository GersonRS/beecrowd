x = int(input())
z = int(input())
while z <= x:
    z = int(input())

count = 0
soma = 0

while soma <= z:
    soma += x
    x += 1
    count += 1

print(count)
