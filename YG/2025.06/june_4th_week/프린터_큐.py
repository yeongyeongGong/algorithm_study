# 문서의 중요도 순으로 출력 예정
# 특정 문서가 출력되는 순서 찾기
from collections import deque


T = int(input())

for _ in range(T):
    N,M = map(int, input().split()) # N: 문서 수, M: 특정문서의 현재 인덱스

    important = list(map(int, input().split()))
    documents = deque(list(enumerate(important)))  # pop진행하면서 인덱스가 변경되기 때문에 enumerate함수를 통해 초기 인덱스값을 함께 저장
    order = 0

    while True:
        idx, importance = documents.popleft()

        if documents:
            max_val = max(documents, key=lambda x: x[1])
            if importance < max_val[1]:
                documents.append((idx, importance))  # 중요도 낮으면 뒤로
            else:
                order += 1
                if idx == M:
                    break
        else:
            order += 1
            if idx == M:
                break
    print(order)







