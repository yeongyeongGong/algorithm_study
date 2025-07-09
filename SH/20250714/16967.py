# 배열 복원하기

H, W, X, Y = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(H + X)]

array = []

for i in range(H):
    subarray = [0] * W
    for j in range(W):
        
        if i - X < 0:
            subarray[j] = field[i][j]
        else:
            if j - Y < 0:
                subarray[j] = field[i][j]
            else:
                subarray[j] = field[i][j] - array[i - X][j - Y]
    array.append(subarray)

for k in range(len(array)):
    print(*array[k])
