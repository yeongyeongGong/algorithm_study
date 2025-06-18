# 뱀

direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
delta = [0, 1, 2, 3]
rotate = {'D': 1, 'L': -1}


def game(x, y, time, to):
    global field  # field 에 있는 사과를 먹으면서, 뱀 길이를 늘려 나간다.

    head = (x, y, time, to)  # 머리와 꼬리가 항상 같은 방향으로 이동하진 않으므로
    tail = (x, y, time, to)  # 두 값을 따로 저장.
    snake = [(head, tail)]
    h_order = 0  # 마찬가지로 머리와 꼬리가 독립적이므로
    t_order = 0  # 방향을 바꾸는 순서도 개별 저장.

    while True:
        # 현재 머리와 꼬리 정보를 추출.
        c_head, c_tail = snake.pop()  # current head, current tail
        ch_r, ch_c, h_time, h_to = c_head  # current head row, current head column
        ct_r, ct_c, t_time, t_to = c_tail  # current tail row, current tail column

        # 머리와 꼬리가 움직일 다음 칸을 저장.
        nh_r, nh_c = ch_r + direction[h_to][0], ch_c + direction[h_to][1]
        nt_r, nt_c = ct_r + direction[t_to][0], ct_c + direction[t_to][1]
        # new head row, new head column / new tail row, new tail column

        if 0 <= nh_r < N and 0 <= nh_c < N:  # 벽에 닿으면 그대로 게임 종료.
            if field[nh_r][nh_c] != 1:  # 몸에 닿으면 그대로 게임 종료.

                # 사과 판별
                # 사과라면 머리만 움직이고, 사과가 아니라면 꼬리까지 움직인다.
                if field[nh_r][nh_c] == 5:
                    h_time += 1
                    nt_r, nt_c = ct_r, ct_c
                else:
                    h_time += 1
                    t_time += 1

                field[nh_r][nh_c] = 1  # 머리 위치에 뱀 그리기.

                # 머리와 꼬리의 회전 판별.
                # 회전한다면 방향을 설정하고,
                # 다음 차례의 timeline 을 보기 위해 order 값에 1을 추가.
                if h_time == timeline[h_order][0]:
                    h_to = (h_to + rotate[timeline[h_order][1]]) % 4
                    h_order += 1
                if t_time == timeline[t_order][0]:
                    t_to = (t_to + rotate[timeline[t_order][1]]) % 4
                    t_order += 1

                # 모든 이동이 끝났으면 머리와 꼬리 정보를 새로 저장.
                snake = [((nh_r, nh_c, h_time, h_to), (nt_r, nt_c, t_time, t_to))]

                # 꼬리가 움직였다면 꼬리 위치를 지우고, 움직이지 않았다면 유지.
                if ct_r != nt_r or ct_c != nt_c:
                    field[ct_r][ct_c] = 0

        # 게임이 끝날 때 1초를 추가하지 않기 때문에, 따로 추가해서 출력.
            else:
                return h_time + 1
        else:
            return h_time + 1


N = int(input())

# 기본 field 설정. (0, 0) 에 뱀이 위치한다.
field = [[0] * N for _ in range(N)]
field[0][0] = 1

# field 에 사과를 입력.
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    field[r - 1][c - 1] = 5

# timeline 설정.
L = int(input())
timeline = []
for _ in range(L):
    X, C = input().split()
    timeline += [(int(X), C)]

# timeline 이 끝났을 때 뱀이 살아있을 수 있기 때문에
# timeline 끝에 빈 입력값 추가.
timeline += [(0, 0)]

result = game(0, 0, 0, 1)

print(result)