# 별의 갯수 9,7,5,3,1,3,5,7,9
# n=5,    2n-1, 2n-3, 2n-5, 2n-7, 2n-9, 2n-7, 2n-5, 2n-3, 2n-1
# 공백 갯수 0,2,4,6,8,6,4,2,0

# 총 9줄
N = int(input())

for i in range(N):
    blank = ' ' * i
    star = '*' * (2*N - 1 - 2*i)
    print(blank + star)

for i in range(N-2,-1,-1):
    blank = ' ' * i
    star = '*' * (2 * N - 1 - 2 * i)
    print(blank + star)