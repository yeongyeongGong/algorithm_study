### 백준 2667 - 단지번호 붙이기
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

'''

N = int(input())
arr=[]
for n in range(N):
    arr.append(list(map(int, input().strip())))

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0 :
            if arr[i][j] == 1 :
                num += 1
                arr[i][j] = num
            for d in range(4) :
                nr = i + dir[d][0]
                nc = j + dir[d][1]
                if 0 <= nr < N and 0 <= nc < N :
                    if arr[nr][nc] == 1 :
                        arr[nr][nc] = arr[i][j]
                    elif arr[nr][nc] > 1 and arr[nr][nc] < num:
                        old = arr[i][j]
                        new = arr[nr][nc]
                        for x in range(N):
                            for y in range(N):
                                if arr[x][y] == old:
                                    arr[x][y] = new

nums=dict()
for ii in range(N):
    for jj in range(N):
        if arr[ii][jj] > 0 :
            if arr[ii][jj] in nums.keys():
                nums[arr[ii][jj]] += 1
            else :
                nums[arr[ii][jj]] = 1
print(len(nums))

fin= sorted(nums.items(), key=lambda x:x[1])
for f in fin:
    print(f[1])