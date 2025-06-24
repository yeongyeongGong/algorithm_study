# 단지번호붙이기

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동남서북.

N = int(input())  # 지도 길이 입력.

field = [list(map(int, input())) for _ in range(N)]  # 지도 구현.
visited = [[0] * N for _ in range(N)]  # 방문한 곳 표시를 위해 2차원 list 제작.

complex = []  # 단지 크기를 입력하기 위한 list 제작.

# 지도의 모든 구역을 확인.
for r in range(N):
    for c in range(N):

        # 집이 있고, 방문하지 않았다면
        if field[r][c] and not visited[r][c]:
            queue = [(r, c)]  # bfs.
            visited[r][c] = 1  # 방문 표시.
            cnt = 1  # 집 갯수 확인.

            while queue:  # queue 를 모두 쓸 때까지 반복.
                cr, cc = queue.pop(0)  # 현재 위치를 찾고,

                # 동남서북 위치를 확인.
                for i in range(4):
                    nr, nc = cr + delta[i][0], cc + delta[i][1]

                    # 범위 안이고,
                    if 0 <= nr < N and 0 <= nc < N:

                        # 집이 있으며 방문하지 않은 곳이라면
                        if field[nr][nc] and not visited[nr][nc]:

                            queue.append((nr, nc))  # queue 에 추가.
                            visited[nr][nc] = 1  # 방문 표시.
                            cnt += 1  # 집 갯수 추가.

            # while 문이 끝났다면 모든 집을 셌으므로 단지 크기에 추가.
            complex.append(cnt)

# 정렬
complex.sort()

# 양식에 맞게 출력. 단지 갯수, 모든 단지의 크기.
print(len(complex), *complex)
