## 백준- 별찍기 9

N = int(input())
for n in range(N, 0,-1):
    print(' ' * (N - n), end='')
    print('*'*(2*n-1))
for n in range(2,N+1):
    print(' ' * (N - n), end='')
    print('*'*(2*n-1))

