# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cleaned = 0
while True:
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned += 1

    # 2. 네 방향 탐색
    moved = False
    for _ in range(4):
        # 왼쪽으로 회전
        d = (d + 3) % 4
        nr, nc = r + dx[d], c + dy[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
            moved = True
            break

    # 3. 네 방향 모두 청소 완료된 경우
    if not moved:
        # 뒤로 한 칸 이동 (방향은 유지)
        back_dir = (d + 2) % 4
        br, bc = r + dx[back_dir], c + dy[back_dir]

        if not (0 <= br < N and 0 <= bc < M and room[br][bc] != 1):
            break
        r, c = br, bc

print(cleaned)
