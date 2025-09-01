# 고속의 숫자 탐색

# idea
# 달려서 벽에 부딛혔을 때 visited 처리를 하고 나면,
# 나중에 걸어서 해당 위치에 도달했을 때 처리를 하지 않는 문제가 생김.
# 하지만, 어차피 달려와서 체크하는 시점이 항상 걸어와서 체크하는 시점보다 빠르므로
# 처리를 해야 하는 이유가 없음.

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동남서북


# bfs 탐색
def bfs(r, c):
    queue = [(r, c, 0)]  # 행, 열, 이동 횟수.
    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1

    while queue:
        cr, cc, cnt  = queue.pop(0)

        # 도착지라면 cnt 출력.
        if field[cr][cc] == 1:
            return cnt

        # 아니라면 동남서북(걸어가기) 순회 후 동남서북(뛰어가기) 순회.
        for i in range(8):

            # 걸을 때
            if i < 4:
                # 범위 안이고
                if 0 <= cr + delta[i][0] < 5 and 0 <= cc + delta[i][1] < 5:
                    # 벽이 아니면
                    if field[cr + delta[i][0]][cc + delta[i][1]] != -1:
                        # 간다.
                        nr, nc = cr + delta[i][0], cc + delta[i][1]
                    # 벽이면 안 간다.
                    else:
                        nr, nc = -1, -1
                # 범위 밖이면 안 간다.
                else:
                    nr, nc = -1, -1

            # 뛰어갈 때
            else:
                # 현재 위치
                nr, nc = cr, cc
                # 이동할 위치
                dr, dc = cr + delta[i - 4][0], cc + delta[i - 4][1]
                # 이동할 위치가 범위 안이고 벽이 아니라면
                while 0 <= dr < 5 and 0 <= dc < 5 and field[dr][dc] != -1:
                    # 이동.
                    nr, nc = dr, dc
                    # 해당 방향으로 계속 뛰어갈 준비.
                    dr, dc = nr + delta[i - 4][0], nc + delta[i - 4][1]
                    # 내 위치가 7이라면 멈춤.
                    if field[nr][nc] == 7:
                        break

            # 가는 상황이라면 가고, cnt 늘려서 queue에 추가.
            if 0 <= nr < 5 and 0 <= nc < 5:
                if not visited[nr][nc]:
                    queue.append((nr, nc, cnt + 1))
                    visited[nr][nc] = 1

    # 못 가는 상황이면 -1 출력.
    return -1


field = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

result = bfs(r, c)
print(result)
