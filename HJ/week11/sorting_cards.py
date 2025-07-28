### 백준 1715 - 카드 정렬하기

'''
3
10
20
40

'''

import heapq

N = int(input())
cards= []
for n in range(N):
    heapq.heappush(cards, int(input()))



cnt= 0
while len(cards) >= 2 :
    now = heapq.heappop(cards)
    now += heapq.heappop(cards)

    cnt += now
    heapq.heappush(cards, now)
    now = 0

print(cnt)

