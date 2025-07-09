# 로봇청소기

delta = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

N, M = map(int, input().split())
r, c, d = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

cnt = 0  # 청소하는 칸의 갯수.
flag = 1  # 아래 while 문 반복 종료 표시자.

while flag:

    # 청소되지 않은 칸이라면 청소한다.
    if not field[r][c]:
        field[r][c] = 2
        cnt += 1
    
    # 청소된 칸이라면 주변 4칸을 살펴본다.
    for direction in range(4):
        dr, dc = r + delta[direction][0], c + delta[direction][1]
        
        # 청소되지 않은 빈 칸이 있는 경우
        if not field[dr][dc]:

            # 반시계 방향으로 90도 회전.
            d = (d - 1) % 4

            # 바라보는 칸을 기준으로,
            nr, nc = r + delta[d][0], c + delta[d][1]
            
            # 청소되지 않은 빈 칸의 경우 한 칸 전진.
            if not field[nr][nc]:
                r, c = nr, nc
            
            # 이후 1번으로 돌아감 = while 문 재시작.
            break

    # 청소되지 않은 칸이 없는 경우
    else:

        # 뒤쪽 칸을 기준으로,
        nr, nc = r - delta[d][0], c - delta[d][1]

        # 갈 수 있다면 간다.
        if field[nr][nc] != 1:
            r, c = nr, nc
        
        # 벽을 만난다면 작동 중지.
        else:
            flag = 0

print(cnt)