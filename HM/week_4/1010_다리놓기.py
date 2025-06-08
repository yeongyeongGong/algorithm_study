memo = {}
def bridge(n, m):
    if m == 0:
        return 1
    elif n < m:
        return 0
    if (n, m) in memo:
        return memo[(n, m)]

    memo[(n, m)] = bridge(n - 1, m - 1) + bridge(n - 1, m)
    return memo[(n, m)]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(bridge(M, N))
