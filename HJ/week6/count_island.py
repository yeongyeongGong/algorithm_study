### 백준 4963 - 섬의 개수

'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

'''

while True:
    w, h = list(map(int, input().split()))
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    if [w, h] == [0, 0]:
        break

    dir = [[-1, 0], [1, 0], [0, -1], [0, 1],[-1, 1], [-1, -1], [1, -1], [1, 1]]  # 상하좌우, 대각선

    num = 1
    for j in range(w):
        for i in range(h):
            if arr[i][j] > 0:
                if arr[i][j] == 1:
                    num += 1
                    arr[i][j] = num
                for d in range(8):
                    nr = i + dir[d][0]
                    nc = j + dir[d][1]
                    if 0 <= nr < h and 0 <= nc < w:
                        if arr[nr][nc] == 1:
                            arr[nr][nc] = arr[i][j]
                        if arr[nr][nc] > 1 and arr[nr][nc] < num:
                            old = arr[i][j]
                            new = arr[nr][nc]
                            for x in range(h):
                                for y in range(w):
                                    if arr[x][y] == old:
                                        arr[x][y] = new

    nums = set()
    for x in range(h):
        for y in range(w):
            if arr[x][y] >= 2:
                nums.add(arr[x][y])
    print(len(nums))





