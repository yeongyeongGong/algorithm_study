# 흰지렁이는 인접 배추를 해충으로부터 지켜줌
# 인접 배추란 상하좌우 + 현위치 배추
# 모든 배추를 지킬 수 있는 최소 지렁이 수를 구하기

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # M-가로,N-세로,K-배추 개수
    cabbage_field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    worm = 0
    for i in range(K):
        X,Y = map(int, input().split()) # 배추 위치 좌표
        cabbage_field[Y][X] = 1





    for row in cabbage_field:
        print(row)
