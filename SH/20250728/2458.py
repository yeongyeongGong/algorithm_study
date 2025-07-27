# 키 순서

# idea
# 내 키가 몇 번째인지 알려면 모든 친구들과의 키 비교가 완료된 친구여야만 한다.
# 즉, 모든 정점을 들를 수 있는 친구여야만 한다.
# 그런데, 정순 배열 뿐만 아니라 역순 배열도 고려해야 한다. 왜? 키는 커지는 순서로만 보고 있으니까.
# 그러니까, 커지는 순서로 친구를 보고, 작아지는 순서로 친구를 본 후에 안 본 친구가 없다면 키 비교가 가능하다.


def bfs(start):  # 나보다 키가 큰 친구들을 모두 확인. (나 포함)
    queue = [start]

    # 나보다 키가 큰 친구들.
    visited = [0] * (N + 1)
    visited[start] = 1

    while queue:
        current = queue.pop(0)
        for i in range(N + 1):
            if field[current][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

    return visited

def reverse_bfs(start):  # 나보다 키가 작은 친구들을 모두 확인. (나 포함)
    queue = [start]

    # 나보다 키가 작은 친구들.
    visited = [0] * (N + 1)
    visited[start] = 1

    while queue:
        current = queue.pop(0)
        for i in range(N + 1):
            if field[i][current] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

    return visited

def fulltrack(start):  # 내가 키 비교가 가능한 학생인지 판별.

    # 각자 키가 크고 작은 친구들의 list를 저장.
    visit = bfs(start)
    reverse_visit = reverse_bfs(start)

    # 키 비교를 한 번도 안 한 친구가 있다면 다른 친구로 넘어감.
    for j in range(1, N + 1):
        if visit[j] == 0 and reverse_visit[j] == 0:
            return 0

    # 키 비교를 전부 했다면 나는 키 비교가 가능한 학생이다.
    else:
        return 1


N, M = map(int, input().split())
field = [[0] * (N + 1) for _ in range(N + 1)]
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    field[a][b] = 1

for k in range(1, N + 1):
    count += fulltrack(k)

print(count)