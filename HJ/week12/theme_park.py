### 백준 1561 - 놀이공원

'''
3 5
7 8 9 7 8

7 2
3 2

22 5
1 2 3 4 5

'''


N,M = map(int, input().split())
lst=list(map(int, input().split()))

if N <= M :
    print(N)
    exit()

def cnt(time) :
    return M + sum(time // lst[i] for i in range(M))

### 이분탐색으로 탑승시간 찾기
time = 0
left = 0
right = max(lst) * N
while left <= right :
    mid = (left+right) // 2

    if cnt(mid) >= N :
        time = mid
        right = mid -1
    elif cnt(mid) < N :
        left= mid + 1

now = time
check = cnt(max(0,now-1))
tmp=[]
for l in range(M):
    if lst[l] >= 0 :
        if now % lst[l] == 0 :
            tmp.append(l)
    else :
        pass

tmp.sort()
for t in tmp :
    check += 1
    if check == N :
        result = t+1
        print(result)
        break