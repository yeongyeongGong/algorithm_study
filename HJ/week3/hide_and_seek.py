## 백준 - 숨바꼭질 1697

from collections import deque
def bfs(start, end):
    visited = [0] * 100001
    move = deque([[start,0]])
    visited[start] = 1

    while move :
        current, cnt = move.popleft()
        if current == end:
            return cnt

        for position in [current+1, current-1, 2*current]:
            if 0 <= position <=100000 and visited[position] == 0:
                move.append([position, cnt+1])
                visited[position] = 1

    return -1

N,K = map(int, input().split())

print(bfs(N,K))