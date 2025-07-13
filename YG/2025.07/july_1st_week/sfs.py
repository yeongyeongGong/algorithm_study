N = 3
arr = ['A', 'B', 'C']

for bit in range(1 << N):  # 0 ~ 7
    subset = []
    for i in range(N):
        if bit & (1 << i):
            subset.append(arr[i])
    print(f"bit = {bit:03b} → subset = {subset}")
