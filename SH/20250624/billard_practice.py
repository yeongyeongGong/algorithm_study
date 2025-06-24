# 당구 연습

# idea
# 단순히 상하좌우 길이의 최솟값을 넣으면 끝.
# 단, 당구대 벽과 평행한 일직선에 공 두 개가 나란히 있는 경우
# 쿠션을 할 수 없는 벽이 존재한다.


def solution(m, n, startX, startY, balls):

    answer = []

    for i in range(len(balls)):  # 목적구 갯수만큼 반복.
        a = balls[i][0]
        b = balls[i][1]  # 목적구의 위치를 변수로 설정.

        # 오른쪽 벽에 원쿠션 하는 경우
        E_x = 2 * m - (startX + a)
        E_y = b - startY

        # 아래쪽 벽에 원쿠션 하는 경우
        S_x = a - startX
        S_y = b + startY

        # 왼쪽 벽에 원쿠션 하는 경우
        W_x = a + startX
        W_y = b - startY

        # 위쪽 벽에 원쿠션 하는 경우
        N_x = a - startX
        N_y = 2 * n - (b + startY)

        # 당구대와 평행한 일직선에 공 두 개가 나란히 있는 경우.
        if startX < a and startY == b:  # 내 공이 왼쪽, 목적구가 오른쪽.
            E = 100000000000000
        else:
            E = E_x ** 2 + E_y ** 2

        if startX == a and startY > b:  # 내 공이 위쪽, 목적구가 아래쪽.
            S = 100000000000000
        else:
            S = S_x ** 2 + S_y ** 2

        if startX > a and startY == b:  # 내 공이 오른쪽, 목적구가 왼쪽.
            W = 100000000000000
        else:
            W = W_x ** 2 + W_y ** 2

        if startX == a and startY < b:  # 내 공이 아래쪽, 목적구가 위쪽.
            N = 100000000000000
        else:
            N = N_x ** 2 + N_y ** 2

        answer.append(min(E, S, W, N))  # 최솟값을 구해 집어넣는다.

    # print(answer)

    return answer


solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])
