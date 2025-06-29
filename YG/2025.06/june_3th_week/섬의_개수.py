# input 0 0 입력 들어오면 stop
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        land_map = [list(map(int, input().split())) for _ in range(h)]
        dx = [1,-1,0,0,1,1,-1,-1]  #하/상/좌/우/좌하/우하/좌상/우상
        dy = [0,0,-1,1,-1,1,-1,1]
        visited = [[False] * w for _ in range(h)]
        island_cnt = 0
        for i in range(h):
            for j in range(w):
                if not visited[i][j] and land_map[i][j] == 1:
                    visited[i][j] = True
                    stack = [(i, j)]

                    while stack:
                        x,y = stack.pop()
                        for k in range(8):
                            nx = x + dx[k]
                            ny = y + dy[k]

                            if 0<= nx < h and 0<= ny < w and visited[nx][ny] == False and land_map[nx][ny] == 1:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                    island_cnt += 1

        print(island_cnt)


    # for row in land_map:
    #     print(row)
    # print('---')