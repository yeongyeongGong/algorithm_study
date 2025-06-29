T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M:가로, N:세로, K:배추 수
    cabbage_field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    worm = 0

    for _ in range(K):
        X, Y = map(int, input().split())  # X: 가로, Y: 세로
        cabbage_field[Y][X] = 1

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

    for i in range(N):         # 시작점 찾기
        for j in range(M):
            if not visited[i][j] and cabbage_field[i][j] == 1:
                visited[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in delta:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if not visited[nx][ny] and cabbage_field[nx][ny] == 1:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                worm += 1

    print(worm)
