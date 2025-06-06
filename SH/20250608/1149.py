# RGB 거리

N = int(input())
cost = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * N

dp[0] = cost[0]

for i in range(1, N):
    dp[i] = (
        min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0],
        min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1],
        min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2],
    )

print(min(dp[-1]))


# 사고의 확장이 필요. dp 라고 꼭 값을 하나만 만들 이유는 없다.