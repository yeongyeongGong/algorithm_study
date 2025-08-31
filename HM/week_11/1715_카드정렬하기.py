'''
제일 효율적이 방법 : 작은 묶음끼리 먼저 더해가기
단순 정렬해서 누적값을 더해가는건 시간초과 걸릴 확률 높음(N 최대값이 100,000)
최소힙 사용
'''
import heapq

heap = []

N = int(input())
for _ in range(N):
    card = int(input())
    heapq.heappush(heap, card)

# 누적합
result = 0

while len(heap) > 1:
    # root에서 작은 수들을 뽑아서 더하고 다시 heap에 넣기
    print(heap)
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += (a + b)
    heapq.heappush(heap, a + b)

print(result)
