# 시간초과남
# 다시 풀기

from collections import deque
import sys
input = sys.stdin.readline

def DFS(start):
    visited[start] = 1
    queue = deque()
    queue.append(start)
    result = True

    while queue:
        current = queue.popleft()
        for node in adj[current]:
            if not visited[node]:
                queue.append(node)
                visited[node] = (visited[current] + 1) % 2
            elif visited[node] == visited[current]:
                result = False
    return result


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)

    visited = [0] * (V + 1)  # 방문기록 저장
    answer = DFS(1)
    if answer:
        print('YES')
    else:
        print('NO')

