# 포도주 시식

n = int(input())
wines = [int(input()) for _ in range(n)]
sum_wines = [0] * n

sum_wines[0] = wines[0]

if n >= 2:
    sum_wines[1] = wines[0] + wines[1]

if n >= 3:
    sum_wines[2] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
    for i in range(3, n):
        sum_wines[i] = max(sum_wines[i - 1], sum_wines[i - 2] + wines[i], sum_wines[i - 3] + wines[i - 1] + wines[i])

print(sum_wines[-1])