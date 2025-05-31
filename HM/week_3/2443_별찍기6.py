N = int(input())

for i in range(N):
    for blank in range(i):
        print(' ', end='')
    for star in range(2*(N-i)-1):
        print('*', end='')
    print()

