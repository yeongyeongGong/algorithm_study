### 백준 14503 - 로봇 청소기

'''
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

4 8
1 4 2
1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1

'''

N, M = map(int,input().split())
R,C,d = map(int, input().split())

dir_first= [[-1,0],[0,1],[1,0],[0,-1]] # 북,동,남,서

arr=[]
for n in range(N):
    arr.append(list(map(int, input().split()))) # 0:청소X, 1:청소O

now = [R,C]
dir_change = [[-1,0],[0,-1],[1,0],[0,1]] # 북서남동
dir_idx = dir_change.index(dir_first[d])
cnt = 0

while True :
    r, c = now
    if arr[r][c] == 0 :
        arr[r][c] = 2
        cnt += 1

    # 네 방향 중 청소안한 곳있으면, 반시계로 돌면서 이동

    for dr in range(1,5):
        idx = (dir_idx+dr)%4

        nr = r + dir_change[idx][0]
        nc = c + dir_change[idx][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 :
            dir_idx = idx
            now = [nr,nc]
            break

    else :
        # 네 방향 모두 청소되어있을 때
        mr, mc = dir_change[(dir_idx+2)%4]
        nr = r + mr
        nc = c + mc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1 :
            now = [nr,nc]
        else :
            break

print(cnt)