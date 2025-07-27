# 퇴사

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

# 점화식이 꼬이지 않게 마감날 그 다음 날 값을 임의로 추가.
dp = [0] * (N + 1)

# 점화식. 가장 마지막 날부터 거꾸로 센다.
for i in range(N - 1, -1, -1):

    # 유효한 날짜라면,
    if i + lst[i][0] <= N:

        # 해당 날짜 이후의 값 중 가장 큰 값을 선택해 추가한다.
        dp[i] = lst[i][1] + max(dp[i + lst[i][0]:])

# 최댓값 출력.
print(max(dp))
