### 백준 - 포도주 시식

'''
6
6
10
13
9
8
1

'''

N = int(input())
cups = []
for n in range(N):
    cups.append(int(input()))
if N == 1 : ## 와인이 한잔 뿐이면 그냥 바로 답 내기
    print(cups[N-1])
else :
    dp = [0] * N
    dp[0] = cups[0]
    dp[1] = cups[1] +dp[0]
    i = 1
    while i < N-1 :
        i += 1
        # print('i', i)
        if i >= 3 :
            # print(dp[i-2] + cups[i], dp[i-1], dp[i-3]+cups[i-1]+cups[i])
            dp[i] = max(dp[i-2] + cups[i], dp[i-1], dp[i-3]+cups[i-1]+cups[i])
        else :

            # print(dp[i-2] + cups[i], dp[i-1], dp[i-1]-cups[i-2]+cups[i])
            dp[i] = max(dp[i-2] + cups[i], dp[i-1], dp[i-1]-cups[i-2]+cups[i])

    print(dp[N-1])