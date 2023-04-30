x, q = map(int, input().split(" "))

valores = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5,
}

print(f"Total: R$ {q*valores.get(x, 0.0):.2f}")
