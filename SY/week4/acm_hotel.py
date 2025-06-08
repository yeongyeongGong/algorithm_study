T = int(input())

for _ in range(T):

    H, W, N = map(int, input().split())

    diff = 0

    if H >= N:
        yy = N
        xx = 1

    else:
        while H < N:
            y = N - H
            diff += 1
            N -= H

            yy = y
            xx = diff+1

    if xx <= 9:
        xx = '0' + str(xx)

    print(str(yy) + str(xx))
