a = [0] * 100


for i in range(len(a)):
    a[i] = float(input())
    if a[i] <= 10:
        print(f"A[{i}] = {a[i]:.1f}")
