T = int(input())

for _ in range(T):
    R, S = input().split()

    for alpha in S:
        print(alpha * int(R), end='')
    print()