alcool = 0
gasol = 0
diesel = 0
while True:
    x = int(input())
    if x == 4:
        break
    elif x == 1:
        alcool += 1
    elif x == 2:
        gasol += 1
    elif x == 3:
        diesel += 1

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasol}")
print(f"Diesel: {diesel}")
