'''
n = 6
vertex : [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3
'''

# ================== 프로그래머스 문제 풀이 =======================
from collections import deque

# BFS 사용
def solution(n, edge):
    answer = 0
    visited = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for n1, n2 in edge:
        adj[n1].append(n2)
        adj[n2].append(n1)
    print(adj)
    queue = deque()
    # 1에서부터 시작하므로 1 추가
    queue.append(1)
    visited[1] = 1

    while queue:
        current = queue.popleft()
        for node in adj[current]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = visited[current] + 1
    max_edge = max(visited)
    for v in range(1, n + 1):
        if visited[v] == max_edge:
            answer += 1
    return answer
# ============================================================

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(n, edge))
