# 지뢰찾기

delta = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1),
]  # 위쪽부터 시계방향 8방향

N = int(input())
field = [list(input()) for _ in range(N)]
new_field = [[0] * N for _ in range(N)]

# 모든 칸을 보면서
for row in range(N):
    for col in range(N):

        # 지뢰 칸이면 지뢰 표시를 한다.
        if field[row][col] != '.':
            new_field[row][col] = '*'
            pass

        # 지뢰가 아니면 인접한 지뢰 갯수를 적는다.
        else:
            for dl in range(8):
                nr, nc = row + delta[dl][0], col + delta[dl][1]
                if 0 <= nr < N and 0 <= nc < N and field[nr][nc] != '.':
                    new_field[row][col] += int(field[nr][nc])

            # 지뢰가 10개 이상이면 많다고 표시한다.
            if new_field[row][col] >= 10:
                new_field[row][col] = 'M'

# 출력.
for i in range(N):
    for j in range(N):
        print(new_field[i][j], end='')
    print()
