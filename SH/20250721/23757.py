# 아이들과 선물 상자

# idea
# 일반적인 방식으로 구현하면 시간이 무조건 터진다.
# heap 을 사용하는 문제. heap 공부 다시 해야겠다....

# heap 에 정보를 넣는 함수.
def heappush(heap, data):

    # 일단 정보를 heap 의 마지막에 추가.
    heap.append(data)

    # 그 정보의 번호를 지정. heap 의 마지막 번호.
    child = len(heap) - 1

    # 그 정보가 최상단에 올 때까지 반복. 중간에 멈출수도 있고...
    while child:

        # 그 정보의 상위 노드를 확인.
        parent = (child - 1) // 2

        # 상위 노드가 해당 노드보다 작다면 둘의 위치를 바꾼다.
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]

            # 이후 둘의 번호도 바꾼다.
            child = parent

        # 상위 노드가 해당 노드보다 크다면 그대로 종료.
        else:
            break

# heap 에서 정보를 추출하는 함수.
def heappop(heap):

    # heap 의 길이가 1이라면 그냥 바로 추출.
    if len(heap) == 1:
        return heap.pop()

    # heap 의 가장 앞 노드를 빼내고, 가장 끝 노드를 제일 위에 설정.
    result = heap[0]
    heap[0] = heap.pop()

    # 가장 위 노드를 내려보내면서 진행하기 위해 부모 노드와 자식 노드를 설정.
    parent, child = 0, 1

    # 자식 번호가 heap 길이보다 커질때 종료한다.
    while child < len(heap):

        # 형제 노드를 설정.
        brother = child + 1

        # 형제 노드가 있고, 그 형제가 해당 노드보다 더 크다면
        if brother < len(heap) and heap[child] < heap[brother]:
            # 그 형제를 움직인다.
            child = brother

        # 부모가 자식보다 작다면 둘의 위치를 교환.
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child

            # 이후 자식 노드번호를 새로 설정.
            child = parent * 2 + 1

        # 부모가 자식보다 크다면 종료.
        else:
            break

    # 뽑은 값을 출력.
    return result


N, M = map(int, input().split())
heap = []
present = list(map(int, input().split()))
children = list(map(int, input().split()))

# 모든 선물상자 크기를 heap 에 입력.
for i in range(N):
    heappush(heap, present[i])

# 선물 상자를 하나씩 뽑아 아이들과 비교.
for j in range(M):
    box = heappop(heap)

    # 선물 상자가 크지 않다면 0 출력 후 종료.
    if box < children[j]:
        print(0)
        quit()

    # 아니라면 계속 진행.
    else:
        heappush(heap, box - children[j])

# 진행이 막힘없이 잘 되면 1 출력.
print(1)