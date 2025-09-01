### 백준 12033 - 김인천씨의 식료품가게(small)


'''
2
3
15 20 60 75 80 100
4
9 9 12 12 12 15 16 20


Case #1: 15 60 75
Case #2: 9 9 12 15

'''

T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    event = []
    for _ in range(n):
        now = lst.pop(0)
        origin = int(now / 3 * 4)
        idx= lst.index(origin)
        event.append(now)
        lst.pop(idx)
    print(f'Case #{t+1}:', end=' ')
    event.sort()
    print(*event)
