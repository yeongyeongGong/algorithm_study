def solve_case(M, N, x, y):
    k = x
    while k <= M * N:
        # y와 같거나 y+N일 경우를 나머지 연산으로 처리
        if (k - y) % N == 0:
            return k
        k += M
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solve_case(M, N, x, y))