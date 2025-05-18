# 러시아 국기 같은 깃발

# idea
# 그냥 완탐.

T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())  # N 줄의 행, M 줄의 열.
    nationalflag = [list(input()) for _ in range(N)]  # 정보를 전부 받아옴.
    count_min = 1000000000  # 최솟값을 찾기 위해 변수 설정.

    for i in range(1, N - 1):  # B 가 시작하는 행을 설정.
        for j in range(i + 1, N):  # R 가 시작하는 행을 설정.
            count = 0  # 색칠하는 횟수를 세기 위해 변수 설정.

            # 0 번째 열 ~ i-1 번째 열까지 W 칠하기
            for W_line in range(0, i):
                for W in range(M):
                    if nationalflag[W_line][W] in ['B', 'R']:
                        count += 1

            # i 번째 열 ~ j-1 번째 열까지 B 칠하기
            for B_line in range(i, j):
                for B in range(M):
                    if nationalflag[B_line][B] in ['W', 'R']:
                        count += 1

            # j 번째 열 ~ N-1 번째 열까지 R 칠하기
            for R_line in range(j, N):
                for R in range(M):
                    if nationalflag[R_line][R] in ['W', 'B']:
                        count += 1

            # 칠한 횟수 비교
            if count < count_min:
                count_min = count

    print(f'#{tc} {count_min}')
