# 로봇청소기

delta = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

N, M = map(int, input().split())
r, c, d = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
flag = 1

while flag:
    if not field[r][c]:
        field[r][c] = 2
        cnt += 1
    
    for direction in range(4):
        dr, dc = r + delta[direction][0], c + delta[direction][1]
        if not field[dr][dc]:
            d = (d + 1) % 4
            nr, nc = r + delta[d][0], c + delta[d][1]
            if not field[nr][nc]:
                r, c = nr, nc
                break
    else:
        nr, nc = r - delta[d][0], c - delta[d][1]

        if field[nr][nc] != 1:
            r, c = nr, nc
        else:
            flag = 0

print(cnt)