# 가지고있는 정수로 만들 수 있는 모든 조합을 구해서
# S가 되는 경우의 수를 구하기

from itertools import combinations

N, S = map(int,input().split()) # N:정수의 개수, S: 구해야하는 정수
arr = list(map(int, input().split()))

cnt = 0

for i in range(1,N+1):
    for comb in combinations(arr, i):
        if sum(comb) == S:
            cnt += 1

print(cnt)

