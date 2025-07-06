from collections import deque

# 도시 개수 : N, 도로 개수 : M, 거리 정보 : K,  출발 도시 정보 : X
N, M, K, X = map(int, input().split())

# 인접 리스트
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

# 최단거리 찾기 : BFS 사용
visited = [-1] * (N + 1)  # 답이 없는 경우도 고려해서 -1로 초기화


def solve_BFS(v):
    queue = deque()
    # 출발 지점 넣기
    queue.append(v)
    visited[v] += 1
    while queue:
        now = queue.popleft()
        for i in adj[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)

solve_BFS(X)

# 최단거리 K인 도시 찾기
result = []
for j in range(N+1):
    if visited[j] == K:
        result.append(j)

if not result:
    print(-1)
else:
    result.sort()
    for n in result:
        print(n)

