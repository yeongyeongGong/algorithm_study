from collections import deque

# 1,1 에서 N,M 까지 도달하기위해서 걸리는 최단 거리
# 각각의 수들은 '붙어서' 입력으로 주어진다.

N,M = map(int, input().split()) #인덱스와 다르게 1,1부터 시작하기 때문에 실제 도달해야하는 위치는 N-1, M-1
maze = [list(map(int, input())) for _ in range(N)]
q=deque()
visit = [[0] * M for _ in range(N)]
q.append((0,0))
visit[0][0]=1

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]  # 4방향 탐색
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:  # 범위 체크
            if visit[nx][ny] == 0 and maze[nx][ny] == 1:   # 방문하지 않았고, 이동 가능한 칸(1)일 때
                q.append((nx, ny))
                visit[nx][ny] = 1
                maze[nx][ny] = maze[x][y] + 1  # 거리 누적

print(maze[N-1][M-1])
