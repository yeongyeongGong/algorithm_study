# ABCDE

def DFS(s, d):
    global result
    if d == 4:  # depth가 4이면 종료
        result = True
        return
    visited[s] = 1
    for i in friend[s]:
        if visited[i] == 0:
            DFS(i, d+1)
            if result:  # 이미 찾으면 미리 종료
                return
    visited[s] = 0


N, M = map(int, input().split())    # N : 사람의 수, M : 친구 관계의 수
friend = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
visited = [0] * N    # 방문처리
depth = 0   # 친구 관계 수
result = False

for s in range(N):
    if result:  # result = True면 미리 종료
        break
    DFS(s, 0)

print(1 if result else 0)