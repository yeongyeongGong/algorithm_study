N = int(input())

for _ in range(N):
    for _ in range(5):
        print('@' * N, end='')
    print()

for _ in range(N*3):
    print('@' * N)

for _ in range(N):
    for _ in range(5):
        print('@' * N, end='')
    print()
