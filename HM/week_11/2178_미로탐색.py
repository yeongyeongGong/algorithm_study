'''
4 6
101111
101010
101011
111011
'''
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if map_info[nr][nc] == 1 and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1


N, M = map(int, input().split())
map_info = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start = (0, 0)
BFS(start)
result = visited[N - 1][M - 1]
print(result)
