### 백준 6064 - 카잉달력(fail)

'''
3
10 12 3 9
10 12 7 2
13 11 5 6

'''
import math

T = int(input())
for t in range(T):
    M,N,x,y = map(int, input().split())
    cnt = 1
    nx = 1
    ny = 1
    max_cnt = math.lcm(M,N)
    while True :
        if nx == x and ny == y :
            break
        if cnt > max_cnt :
            cnt = -1
            break
        if nx < M :
            nx +=1
        else :
            nx = 1

        if ny < N :
            ny +=1
        else :
            ny =1
        cnt +=1

    print(cnt)
