def solve():
    # 델타
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    n = 2  # 2초부터 시작
    # N초까지 반복
    while n <= N:
        for i in range(R):
            for j in range(C):
                # 짝수 시간에는 폭탄 설치
                # 기존 폭탄은 X로 치환, 새로 설치하는 폭탄은 O로 표시
                if n % 2 == 0:
                    if bomb_map[i][j] == '.':
                        bomb_map[i][j] = 'O'
                    elif bomb_map[i][j] == 'O':
                        bomb_map[i][j] = 'X'

                # 홀수 시간에는 폭탄 폭발
                # X 표시된 폭탄만 폭발(시간 되었으니 폭발)
                if n % 2 == 1:
                    if bomb_map[i][j] == 'X':
                        bomb_map[i][j] = '.'
                        for d in range(4):
                            nr = i + dr[d]
                            nc = j + dc[d]
                            if 0 <= nr < R and 0 <= nc < C:
                                # 만약 인근에 있는게 폭탄이면 패스..
                                # 시간이 되서 터져야하는건 X, X 폭탄은 동시에 폭발
                                # 폭탄은 연쇄폭발이 안 일어나므로 O폭탄은 터져도 그것만 없어지면 됨
                                if bomb_map[nr][nc] == 'X':
                                    pass
                                else:
                                    bomb_map[nr][nc] = '.'
        # 시간 증가
        n += 1


R, C, N = map(int, input().split())
bomb_map = []
for _ in range(R):
    x = list(input())
    bomb_map.append(x)

solve()

# for row in bomb_map:
#     print(*row)
for r in range(R):
    for c in range(C):
        # X 표시된 폭탄 O로 바꾸기
        if bomb_map[r][c] == 'X':
            print('O', end='')
        else:
            print(bomb_map[r][c], end='')
    print()
