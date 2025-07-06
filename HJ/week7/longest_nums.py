### 백준 11053 - 가장 긴 증가하는 부분 수열

'''
6
10 20 10 30 20 50

6
10 30 20 30 40 50

'''

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

## 시도했던거 - 리스트 전체 저장하기
# N = int(input())
# arr = list(map(int, input().split()))
# if N == 1 :
#     print(1)
#     exit()
#
# dp=[0]*N
#
# dp[0] = [arr[0]]
# for i in range(1,N):
#     if i == 1 :
#         if arr[i] > dp[i-1][0] :
#             dp[i] = [dp[i-1][0]] + [arr[i]]
#         else :
#             dp[i] = [arr[i]]
#     else :
#         dp[i] = dp[i-1]
#         if arr[i] > dp[i-1][-1] :
#             dp[i] = dp[i-1] + [arr[i]]
#
#         elif arr[i] > dp[i-1][i-2] :
#             dp[i] = dp[i-1][:i-1] + [arr[i]]
#
# print(len(dp[-1]))

