### 백준 - 봄버맨
'''
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

'''

from pprint import pprint
R,C,N = map(int, input().split())
arr=[]
for r in range(R):
    arr.append(list(input().strip()))

n = 0 ## 1초에는 아무것도 하지않음
for i in range(R):
    for j in range(C):
        if arr[i][j] != '.':
            if arr[i][j] == 'O':
                arr[i][j] = 1

while n < N :
    n += 1
    ## 더하기는 항상
    for ii in range(R):
        for jj in range(C):
            if arr[ii][jj] not in  ['.','O'] :
                arr[ii][jj] += 1

    ## 터지기 3이상 홀수일때만
    if n >= 3 and n % 2 == 1 :
        for i in range(R):
            for j in range(C):
                if arr[i][j] in [3,4] :
                    arr[i][j] = '.'
                    if i-1 >= 0 and arr[i-1][j] not in [3,4]:
                        arr[i-1][j] = '.'
                    if i+1 < R  and arr[i+1][j] not in [3,4]:
                        arr[i+1][j] = '.'
                    if j-1 >= 0 and arr[i][j-1] not in [3,4]:
                        arr[i][j-1] = '.'
                    if j+1 < C and arr[i][j+1]  not in [3,4]:
                        arr[i][j+1] = '.'
        for ii in range(R):
            for jj in range(C):
                if arr[ii][jj] == 'x':
                    arr[ii][jj] = '.'
    ## 설치 2이상 짝수 일때만
    elif n >= 2 and n % 2 == 0 :
        for i in range(R):
            for j in range(C):
                if arr[i][j] != '.' :
                    if arr[i][j] == 'O' :
                        arr[i][j] = 0
                else :
                    arr[i][j] = 0
    # print('#',n)
    # pprint(arr)
for x in range(R):
    for y in range(C):
        if arr[x][y] == '.' :
            arr[x][y] = '.'
        else :
            arr[x][y] = 'O'

for xx in range(R):
    for yy in range(C):
        print(arr[xx][yy], end='')
    print()