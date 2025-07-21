T =  int(input())

for _ in range(T):
    M,N,x,y = map(int, input().split())

    X = 1
    Y = 1
    year = 1
    a,b = M,N

    while(b>0):     # 최대 공약수
        a,b = b, a%b

    max_year = M * N / a  # 카잉 달력의 마지막해는  M과 N의 최소공배수

    while year != max_year:
        if X < M:
            X += 1
        else:
            X = 1
        if Y < N:
            Y += 1
        else:
            Y = 1

        year += 1

        if X == x and Y == y:
            print(year)
            break
        elif X != x and Y !=y and year == max_year:
            print(-1)
            break