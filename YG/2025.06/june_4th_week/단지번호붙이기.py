# 정사각형 내에 있는 그래프의 갯수(단지수)를 구하고
# 각 그래프의 노드 갯수(단지에 속하는 집의 수) 구하기
# 구하고 오름차순으롤 정렬해서 출력

N = int(input())    # 정사각형 크기
house_map = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
house_cnt = []  #단지별 cnt를 저장해 놓는 배열
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and house_map[i][j] == 1: # 그래프 시작점 찾아주기
            visited[i][j] = True
            stack = [(i, j)]
            cnt = 1 # 단지별 집 수

            # stack이 true일 동안
            # 즉 인접해 있는 한 단지(그래프)를 다 도는 동안
            while stack:
                x,y = stack.pop()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if house_map[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                            cnt += 1    #단지별 집 수
            house_cnt.append(cnt)

house_cnt.sort()
print(len(house_cnt))  # 단지 수
for r in house_cnt:
    print(r)  # 단지별 집 수

