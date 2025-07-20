N, M = map(int, input().split())
rr, rc, rd = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 순서대로 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = 0

while True:
    # 현재 칸이 청소가 안 되어있으면 청소하기
    if room[rr][rc] == 0:
        room[rr][rc] = -1
        result += 1

    # 현재 칸 중심으로 주변 4칸 중 청소 안 된 곳이 있는 경우
    # 현재 칸에서 바라보는 방향을 시작으로 반시계 방향으로 회전하면서 확인
    # 반시계 방향 회전 : 북 > 서 > 남 > 동 > 북... >> 0 > 3 > 2 > 1 > 0 ...
    for _ in range(4):
        rd = (rd + 3) % 4
        nr = rr + dr[rd]
        nc = rc + dc[rd]

        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0:   # 청소 안된 칸이 있는 경우
                rr = nr
                rc = nc
                break
    else:   # 청소 안된 칸이 없는 경우
        # 후진 방향 찾기
        back = (rd + 2) % 4
        br = rr + dr[back]
        bc = rc + dc[back]
        # 벽이 아니면 후진하기
        if room[br][bc] != 1:
            rr = br
            rc = bc
        # 벽이면 이동 불가 >> 갇혔으니 멈춤
        else:
            break

print(result)