# 적록색약

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동남서북
find = {'R': 1, 'G': 1, 'B': 2}  # 적록색약 판별용 dictionary.


# 일반인 bfs
def bfs_normal(x, y):
    global normal, normal_count

    # 확인한 곳이라면 패스.
    if normal[x][y]:
        return

    # 확인해야 하는 곳이라면 bfs.
    else:
        queue = [(x, y)]
        normal[x][y] = 1

        while queue:
            cr, cc = queue.pop(0)
            for i in range(4):
                nr, nc = cr + delta[i][0], cc + delta[i][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if field[nr][nc] == field[cr][cc] and not normal[nr][nc]:
                        normal[nr][nc] = 1
                        queue.append((nr, nc))

        # 다 돌고 나면 그만큼의 덩어리를 갯수에 추가.
        normal_count += 1
        return

# 적록색약 bfs.
def bfs_colorblind(x, y):
    global normal, colorblind_count

    # 확인한 곳이라면 패스.
    if colorblind[x][y]:
        return

    # 확인해야 하는 곳이라면 bfs.
    else:
        queue = [(x, y)]
        colorblind[x][y] = 1

        while queue:
            cr, cc = queue.pop(0)
            for i in range(4):
                nr, nc = cr + delta[i][0], cc + delta[i][1]
                if 0 <= nr < N and 0 <= nc < N:

                    # 적록색약이면 R 과 G 가 똑같아 보인다.
                    if find[field[nr][nc]] == find[field[cr][cc]] and not colorblind[nr][nc]:
                        colorblind[nr][nc] = 1
                        queue.append((nr, nc))

        # 다 돌고 나면 그만큼의 덩어리를 갯수에 추가.
        colorblind_count += 1
        return


N = int(input())

field = [list(input()) for _ in range(N)]  # 기본 필드.
normal = [[0] * N for _ in range(N)]  # 일반인용 visited.
colorblind = [[0] * N for _ in range(N)]  # 적록색약용 visited.
normal_count = 0  # 일반인 구역 갯수.
colorblind_count = 0  # 적록색약 구역 갯수.

# 모든 곳에서 두 함수를 돌린다.
for r in range(N):
    for c in range(N):
        bfs_normal(r, c)
        bfs_colorblind(r, c)

print(normal_count, colorblind_count)
