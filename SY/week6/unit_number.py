N = int(input())
whole_map = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
unit_cnt = []
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(N):
    for j in range(N):

        if whole_map[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            stack = [(i, j)]
            tmp_cnt = 1

            while stack:
                x, y = stack.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if whole_map[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            stack.append((nx, ny))
                            tmp_cnt += 1

            unit_cnt.append(tmp_cnt)

sorted_unit_cnt = sorted(unit_cnt)

print(len(sorted_unit_cnt))
for num in sorted_unit_cnt:
    print(num)
