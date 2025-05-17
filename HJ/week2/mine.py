### 백준 지뢰찾기 1996

N = int(input())
arr= []
for n in range(N):
    arr.append(list((input().strip())))

## 상하좌우, (대각선) 우상 우하 좌하 좌상
dr = [-1,1,0,0,-1,1,-1,1]
dc = [0,0,-1,1,1,1,-1,-1]
for i in range(N):
    for j in range(N):
        score= 0
        for d in range(8):
            nr = i + dr[d]
            nc = j + dc[d]

            if 0 <= nr < N and 0 <= nc < N :
                if arr[nr][nc] != '.' and arr[nr][nc] in ['1','2','3','4','5','6','7','8','9']:
                    score += int(arr[nr][nc])
        if arr[i][j] not in ['1','2','3','4','5','6','7','8','9']:
            arr[i][j] = score

for x in range(N):
    for y in range(N):
        if arr[x][y] in ['1','2','3','4','5','6','7','8','9'] :
            arr[x][y] = '*'
        elif arr[x][y] >= 10 :
            arr[x][y] = 'M'


for line in arr:
    for l in line:
        print(l,end='')
    print()