N, M = map(int,input().split())

plant = impossible = 0

record = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = input().split()

    if c == '0':
        b = 'N' + b

    record[int(a)].append(b)

for i in range(1, N+1):
    if 'M' in record[i] or 'NP' in record[i]:
        impossible += 1

    if 'P' in record[i] and 'NM' in record[i]:
        plant += 1

print(plant, N-impossible)