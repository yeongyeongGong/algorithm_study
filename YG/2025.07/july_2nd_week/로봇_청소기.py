N,M = map(int, input().split()) # 방의 크기
# d 방향 : 0북쪽,1동쪽,2남쪽,3서쪽
r,c,d = map(int, input().split())   # r,c: 청소기의 첫 좌표, d: 청소기가 바라보는 방향
room = [list(map(int, input().split())) for _ in range(N)]
clean_cnt = 0
delta = [(-1,0),(0,1),(1,0),(0,-1)] # 전진 좌표
reverse_delta = [(1,0),(0,-1),(-1,0),(0,1)] # 후진 좌표

while True:

    if room[r][c] == 0:
        room[r][c] = 3
        clean_cnt += 1
    dd = d
    moved = False
    for _ in range(4):
        dd = (dd + 3) % 4  # (d+4-1)을 4로 나눈 나머지 (반시계 90도회전)
        nx = r + delta[dd][0]  # 현재 좌표에서 전진 좌표
        ny = c + delta[dd][1]

        if 0<= nx < N and 0<= ny < M and room[nx][ny] == 0: # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            r = nx
            c = ny
            d = dd
            moved = True
            break
    if moved:   # 방향이동해서 청소했으면 아래 로직 건너뛰기
        continue
    # 4방향 모두 이미 청소되어있거나, 벽인경우
    nx = r + reverse_delta[d][0]    # 후진준비
    ny = c + reverse_delta[d][1]
    if 0<= nx < N and 0<= ny < M and room[nx][ny] != 1:   # 이미 청소된 곳이라면 후진
        r = nx
        c = ny
        continue
    elif 0<= nx < N and 0<= ny < M and room[nx][ny] == 1 :    # 벽이라면
        print(clean_cnt)    # 방청소 횟수 출력하고
        exit()              # 청소 끝


