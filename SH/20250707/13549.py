# 숨바꼭질 3

N, K = map(int, input().split())

visited = [100001] * 100001
queue = [(N, 0)]
pointer = 0

while pointer < len(queue):
    cur, sec = queue[pointer]
    pointer += 1

    if visited[K] != 100001:
        if sec >= visited[K]:
            continue

    if 0 <= cur <= 100000:
        if sec < visited[cur]:
            visited[cur] = sec
            if 0 <= cur * 2 <= 100000:
                queue.append((cur * 2, sec))
            if 0 <= cur - 1 <= 100000:
                queue.append((cur - 1, sec + 1))
            if 0 <= cur + 1 <= 100000:
                queue.append((cur + 1, sec + 1))

print(visited[K])