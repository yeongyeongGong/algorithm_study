from collections import deque

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)

result = [0] * (V + 1)  # 신뢰도 체크
# 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 = 신뢰를 많이 받는 컴퓨터
def solve(v):
    visited = [0] * (V + 1)  # 방문 체크
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        now = queue.popleft()
        for i in adj[now]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] += 1
                queue.append(i)

for n in range(1, V + 1):
    solve(n)

max_value = max(result)
for j in range(1, V + 1):
    if result[j] == max_value:
        print(j, end=' ')