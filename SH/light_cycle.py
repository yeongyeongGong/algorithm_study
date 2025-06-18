# 빛의 경로 사이클

# idea
# 모든 경로를 입력해서 하나의 경로를 만들어야 할 것처럼 보이지만, 아니다.
# 같은 격자를 같은 방향으로 한 번이라도 지나가는 순간
# 그 경로는 이전의 경로와 같은 경로가 된다.
# 따라서, (격자 행, 격자 열, 방향)이 한 번도 겹치지 않는 것만 세어야 한다.


def solution(grid):

    delta = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}  # 동남서북
    field = [list(grid[i]) for i in range(len(grid))]  # 입력 정보 field 에 저장.
    R = len(field)  # row 갯수.
    C = len(field[0])  # column 갯수.

    def turn(r, c, to):  # 다음 격자를 확인하는 함수.
        if field[r][c] == 'S':  # S 는 직진.
            pass  # to 값이 바뀔 필요가 없다.
        elif field[r][c] == 'L':  # L 은 좌회전.
            to = (to - 1) % 4  # to 값에서 1을 뺀다.
        else:  # R 은 우회전.
            to = (to + 1) % 4  # to 값에서 1을 더한다.

        # r, c 값을 수정. 범위를 벗어나면 반대편으로 간다.
        r, c = (r + delta[to][0]) % R, (c + delta[to][1]) % C

        return r, c, to  # 출력.

    route = set()  # 경로를 확인하기 위해 set 제작.
    answer = []

    for r in range(R):
        for c in range(C):
            for to in range(4):
                cnt = 0  # 경로 갯수를 세는 변수.

                # 없는 경로라면 route 에 입력하고, 방향을 바꾼 후 cnt + 1 한다.
                while (r, c, to) not in route:
                    route.add((r, c, to))
                    r, c, to = turn(r, c, to)
                    cnt += 1

                # cnt 가 0이라면 경로가 겹치는 것.
                if cnt:
                    answer.append(cnt)

    answer.sort()  # 오름차순으로 출력한다.
    # print(answer)

    return answer


solution(["SL", "LR"])
solution(["S"])
solution(["R", "R"])