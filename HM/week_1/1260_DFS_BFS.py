from collections import deque
import sys
input = sys.stdin.readline

def DFS(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end= ' ')
        for i in range(V, 0, -1):
            if adj[v][i] == 1 and not visited[i]:
                stack.append(i)

def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    print(start, end=' ')
    while queue:
        v = queue.popleft()
        for i in range(1, V+1):
            if adj[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1
                print(i, end=' ')


V, E, s = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b = map(int,input().split())
    adj[a][b] = 1
    adj[b][a] = 1
    
visited = [0] * (V + 1)
DFS(s)
print()
visited = [0] * (V + 1)
BFS(s)
