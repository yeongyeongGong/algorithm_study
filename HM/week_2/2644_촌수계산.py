import sys
input = sys.stdin.readline
def solve(start, end):
    # 시작점 설정
    stack = [start]
    visited[start] = 1

    while stack:
        now = stack.pop()
        if now == end:
            break
        for i in range(n+1):
            if adj[now][i] and not visited[i]:
                stack.append(i)
                # 방문 리스트에 촌수 계산해서 넣기
                visited[i] = visited[now] + 1
    if visited[end]:
        # 시작점 방문값을 1로 설정했기에 시작점 값(1)을 빼기
        return visited[end] - 1
    else:
        return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
adj = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
visited = [0] * (n+1)
result = solve(start, end)
print(result)
