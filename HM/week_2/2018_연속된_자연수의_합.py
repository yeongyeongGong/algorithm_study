import sys
import time

input = sys.stdin.readline

N = int(input())

count = 1   # 자기 자신(N) 경우 포함

# 아래 코드는 런타임 에러발생
# for i in range(1, N//2+1):
#     sum = i
#     for j in range(i+1, N+1):
#         sum += j
#         if sum == N:
#             count += 1
#             break
#         if sum > N:
#             break
#
# print(count)

start_idx = 1   # 시작 지점을 가리킴
end_idx = 1     # 마지막 지점을 가리킴
sum = 1

# 마지막 지점이 N이 될때까지 반복
while end_idx != N:
    if sum < N:
        end_idx += 1
        sum += end_idx
    elif sum > N:
        sum -= start_idx
        start_idx += 1
    else:   # sum == N
        count += 1
        end_idx += 1
        sum += end_idx
print(count)