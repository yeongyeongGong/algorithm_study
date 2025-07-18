### 백준 24511 - queuestack

'''

4
0 1 1 0
1 2 3 4
3
2 4 7

1 2 3 4
>>2

선입선출
선입후출

2 1 > 2 >> 1
1 2 > 2 >> 1
1 3 > 3 >> 1
1 4 > 1 >> 4

'''

from collections import deque

N = int(input())
status = list(map(int, input().split()))
data = list(map(int, input().split()))
M = int(input())
add = list(map(int, input().split()))
real=deque()
for i in range(N):
    if status[i] == 0 :
        real.append(data[i])

result =  []
for m in range(M):
    real.appendleft(add[m])
    result.append(real.pop())

print(*result)
