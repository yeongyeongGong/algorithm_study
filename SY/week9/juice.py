N = int(input())

for TC in range(1,N+1):
    people = int(input())

    print(f'#{TC}', end=' ')
    for i in range(people):
        print(f'1/{people}', end=' ')

    print()