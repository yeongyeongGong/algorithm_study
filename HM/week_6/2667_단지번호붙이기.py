'''
5
01001
11011
00001
11100
11111
'''
import sys
from collections import deque

N = int(input())  # 지도 크기
map_data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]  # 지도 데이터

# 델타
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 방문 기록
visited = [[0] * N for _ in range(N)]

# 단지 내 가구 수 기록
complex = []

for r in range(N):
    for c in range(N):
        # 단지 내 가구 수 계산
        count = 0
        # r,c 가 1이고 방문한 적 없는 경우
        if map_data[r][c] == 1 and visited[r][c] == 0:
            visited[r][c] = 1
            count += 1
            queue = deque([(r, c)])
            # 이후 BFS 이용해서 연결된 가구 수 계산
            while queue:
                cr, cc = queue.popleft()
                # 상하좌우 검색
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    if 0 <= nr < N and 0 <= nc < N:
                        if map_data[nr][nc] == 1 and visited[nr][nc] == 0:
                            queue.append((nr, nc))
                            visited[nr][nc] = 1
                            count += 1
            complex.append(count)
print(len(complex))
for c in sorted(complex):
    print(c)
