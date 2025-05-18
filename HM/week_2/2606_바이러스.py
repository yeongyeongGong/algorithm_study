import sys
input = sys.stdin.readline

def DFS(start):
    # 시작점 설정
    stack = [start]
    visited[start] = 1
    count = 0

    while stack:
        current = stack.pop()
        for i in adj[current]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                count += 1
    return count
# V : 정점, E : 간선
V = int(input())
E = int(input())

# 인접리스트
adj = [set() for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)
# 방문체크 리스트
visited = [0]*(V+1)
result = DFS(1)

print(result)