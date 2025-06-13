# 알파벳


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동남서북


def dfs(cr, cc, cnt):  # 재귀 형태의 dfs
    global visited, L

    if L < cnt:  # 최대길이를 갱신
        L = cnt

    for i in range(4):  # 4방향을 확인하면서
        nr, nc = cr + delta[i][0], cc + delta[i][1]
        if 0 <= nr < R and 0 <= nc < C:
            if field[nr][nc] not in visited:  # 해당 위치 알파벳을 사용하지 않았다면
                visited.add(field[nr][nc])  # 추가 후
                dfs(nr, nc, cnt + 1)  # 재귀
                visited.remove(field[nr][nc])  # 추가했던 알파벳 제거

    return

R, C = map(int, input().split())

field = [list(input()) for _ in range(R)]
visited = set()
visited.add(field[0][0])
L = 0

dfs(0, 0, 1)

print(L)
