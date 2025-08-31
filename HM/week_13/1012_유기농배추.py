# 유기농 배추
from collections import deque


def BFS(y, x):
    # 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((y, x))  # 큐에 삽입
    visited[y][x] = 1

    while queue:
        cy, cx = queue.popleft()  # 큐에서 꺼내기
        # 해당 위치에서 상하좌우 탐색
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if field[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]  # 배추밭
    visited = [[0] * M for _ in range(N)]  # 방문처리
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    worm = 0  # 필요한 지렁이 수
    # 배추밭 전체 탐색
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0:  # 배추가 있고 방문한 적 없으면                BFS(i, j)
                BFS(i, j)
                worm += 1
    print(worm)