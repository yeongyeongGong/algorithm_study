# 촌수계산

def bfs(start, end):
    queue = [(start, 0)]  # 시작점, 시작점부터 떨어진 거리
    visited = [0] * n
    visited[start] = 1

    while queue:
        (current, far) = queue.pop(0)
        # 현재 지점이 종료 지점이라면 거리를 반환.
        if current == end:
            return far
        # 아니라면 거리 추가해주고 진행.
        for i in range(n):
            if field[current][i] and not visited[i]:
                queue.append((i, far + 1))
                visited[i] = 1
    # 종료 지점을 못 만났다면 -1 반환.
    return -1


n = int(input())
start, end = map(int, input().split())
field = [[0] * n for _ in range(n)]

m = int(input())
for _ in range(m):
    # 모든 연결된 곳에 1을 적되, 0번부터 시작되므로 값에 -1을 해 준다.
    r, c = map(int, input().split())
    field[r - 1][c - 1] = 1
    field[c - 1][r - 1] = 1

# 마찬가지로 시작점, 끝점 또한 -1을 해 준다.
result = bfs(start - 1, end - 1)
print(result)
