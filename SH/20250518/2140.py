# 지뢰찾기

delta = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1),
]  # 위부터 시계방향으로 8방향

N = int(input())
field = [list(input()) for _ in range(N)]
count = 0

# N 길이가 많이 짧다면 지뢰가 있을 공간이 없다.
if N in (1, 2):
    print(count)

else:
    # str 형태의 숫자를 int 로 변경.
    for i in range(N):
        for j in range(N):
            if field[i][j] != '#':
                field[i][j] = int(field[i][j])

    # 모든 칸의 인접 칸을 보되
    for r in range(N):
        for c in range(N):

            # 안쪽 칸만 본다.
            if field[r][c] == '#':
                for dl in range(8):
                    nr, nc = r + delta[dl][0], c + delta[dl][1]

                    # 인접한 칸이 0이다. == 해당 칸은 지뢰가 없다.
                    if field[nr][nc] == 0:
                        break
                else:
                    for dl in range(8):
                        nr, nc = r + delta[dl][0], c + delta[dl][1]
                        # 지뢰가 있는 칸에 인접한 모든 숫자 칸에서 1을 뺀다.
                        if field[nr][nc] != '#':
                            field[nr][nc] -= 1

                    # 처리가 끝나면 지뢰를 하나 센다.
                    count += 1

    print(count)
