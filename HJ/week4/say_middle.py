### 백준 - 1655 가운데를 말해요

'''

7
1
5
2
10
-99
7
5


'''
#
# N = int(input())
# lst = []
# for n in range(N):
#     tmp = int(input())
#     if lst :
#         if len(lst) == 1 :
#             if lst[0] > tmp:
#                 lst.insert(0, tmp)
#             else :
#                 lst.append(tmp)
#         else :
#             i=0
#             while i < len(lst)-1 :
#                 if lst[i] < tmp <= lst[i+1] :
#                     lst.insert(i+1, tmp)
#                     break
#                 elif lst[i] > tmp :
#                     lst.insert(0, tmp)
#                     break
#                 i += 1
#             else :
#                 lst.append(tmp)
#
#     else :
#         lst.insert(0,tmp)
#
#     print(lst[n//2])

import sys
import heapq

input = sys.stdin.readline
N = int(input())

max_heap = []  # 중앙값 이하 (최대 힙 역할, 음수로 저장)
min_heap = []  # 중앙값 초과 (최소 힙)

for _ in range(N):
    num = int(input())

    # 1. max_heap에 먼저 삽입 (음수로)
    heapq.heappush(max_heap, -num)

    # 2. max_heap에서 가장 큰 값을 min_heap으로 이동
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # 3. 힙 크기 조정 (max_heap이 항상 같거나 1 더 크도록)
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # 4. 중앙값 출력 (max_heap 루트)
    print(-max_heap[0])