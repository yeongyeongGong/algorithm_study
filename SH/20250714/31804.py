# Chance!

# idea
# 일단, 숫자가 많고 큰 경우에는 deque 사용이 불가피하다...
# bfs 이기 때문에 처음 visited 한 후에 다음 visited 는 무조건 시행횟수가 더 많다.
# 따라서, visited 를 체크해야 하는데, chance 를 사용했느냐 하지 않았냐에 따라
# visited 를 다르게 만들어야 한다. 즉, visited 를 두 갈래로 만들어야 한다.

from collections import deque

a, b = map(int, input().split())

# deque 사용.
dq = deque()
dq.append((a, 0, 0))

# 두 갈래의 visited 제작.
visited = [[0] * 2 for _ in range(b + 1)]

# 시작 정보 visited 표시.
visited[a][0] = 1

# 모든 deque 를 사용할 때까지 반복.
while dq:

    # deque 는 이중 연결 list 이기 때문에 수정, 삭제 속도가 O(1) 이다.
    value, count, used = dq.popleft()

    # 값이 나오면 출력.
    if value == b:
        print(count)
        quit()

    # + 1 입력.
    plus = value + 1
    if plus <= b and not visited[plus][used]:
        visited[plus][used] = 1
        dq.append((plus, count + 1, used))

    # * 2 입력.
    multi = value * 2
    if multi <= b and not visited[multi][used]:
        visited[multi][used] = 1
        dq.append((multi, count + 1, used))

    # * 10 입력. 단, chance 를 사용하지 않은 경우에만.
    if not used:
        chance = value * 10
        if chance <= b and not visited[chance][1]:
            visited[chance][1] = 1
            dq.append((chance, count + 1, 1))
