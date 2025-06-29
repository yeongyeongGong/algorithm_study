# 루트 없는 트리가 주어진다.
# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하기
# 1부터 돌면서 부모 노드를 저장

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [0] * (N + 1)

for _ in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

stack = [1]
visited[1] = 1

while stack:
    node = stack.pop()
    for child in graph[node]:
        if not visited[child]:
            visited[child] = 1
            parent[child] = node
            stack.append(child)

for i in range(2, N + 1):
    print(parent[i])
