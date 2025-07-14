# 아이들과 선물 상자


def heappush(heap, data):
    heap.append(data)
    child = len(heap) - 1
    
    while child:
        parent = (child - 1) // 2
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
        else:
            break

def heappop(heap):
    
    if len(heap) == 1:
        return heap.pop()
    
    result = heap[0]
    heap[0] = heap.pop()

    parent, child = 0, 1

    while child < len(heap):
        brother = child + 1

        if brother < len(heap) and heap[child] < heap[brother]:
            child = brother
        
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2 + 1
        else:
            break
    
    return result


N, M = map(int, input().split())
heap = []
present = list(map(int, input().split()))
children = list(map(int, input().split()))

for i in range(N):
    heappush(heap, present[i])

for j in range(M):
    box = heappop(heap)
    if box < children[j]:
        print(0)
        quit()
    else:
        heappush(heap, box - children[j])

print(1)