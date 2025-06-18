### 백준 - 1149 RGB 거리
'''
3
26 40 83
49 60 57
13 89 99

4
5 4 3
1 1 2
1 5 1
5 3 2


'''

N = int(input())
house=[]
dp = [[0]*3 for _ in range(N)]
for n in range(N):
    house.append(list(map(int, input().split())))

dp[0] = house[0]
for i in range(1, N) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]

print(min(dp[N-1]))