# 동적 계획법
import sys

input = sys.stdin.readline

X = int(input())

dp = [0] * (X + 1)

# dp[1] = 1은 연산할 필요가 없으므로 0
dp[1] = 0
for i in range(2, X + 1):
    dp[i] = dp[i-1] + 1 # -1 연산 체크
    # -1 연산과 /2, /3 연산 중 횟수가 적은 걸로
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[X])