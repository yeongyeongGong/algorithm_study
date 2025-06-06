# 참외밭

def first(x):  # 겹치는 방향 중 첫 번째를 고르는 함수.
    a = 0
    b = 0
    for i in range(6):
        if direct[i] == x:
            if not a:
                a = i + 1
            else:
                b = i + 1
    if abs(a - b) > 2:
        return b - 1
    else:
        return a - 1

def last(x):  # 겹치는 방향 중 두 번째를 고르는 함수.
    a = 0
    b = 0
    for i in range(6):
        if direct[i] == x:
            if not a:
                a = i + 1
            else:
                b = i + 1
    if abs(a - b) > 2:
        return a - 1
    else:
        return b - 1


cham = int(input())  # 밭의 단위 참외 수를 입력.
shape = {'a': {1, 3}, 'b': {2, 3}, 'c': {2, 4}, 'd': {1, 4}}  # 밭의 모양을 결정.
minus_shape = {
    'a': [1, 3], 'b': [3, 2], 'c': [2, 4], 'd': [4, 1]
}  # 겹치는 방향의 순서를 결정.

direct = [0] * 6  # 방향.
far = [0] * 6  # 길이.
stack = set()  # 겹치지 않는 set.
rotate = set()  # 겹치는 set. stack 과 rotate 를 통해 shape 를 결정할 수 있음.
field = 1  # 전체 넓이
minus = 1  # 빼야 하는 넓이

for i in range(6):  # 값을 입력하면서 방향, 길이, 모양을 결정.
    direction, how_far = map(int, input().split())
    direct[i] = direction
    far[i] = how_far
    if direction not in stack:
        stack.add(direction)
    else:
        rotate.add(direction)

for j in shape:  # 모양을 결정해서 그 모양에 맞는 순서를 idx 로 설정.
    if shape[j] == rotate:
        idx = minus_shape[j]

for k in range(6):  # 겹치지 않는 두 변을 곱하면 전체 넓이가 된다.
    if direct[k] not in rotate:
        field *= far[k]

for l in range(2):  # 겹치는 두 변 중 잘 선택하면 빼야 하는 넓이가 된다.
    if not l:
        minus *= far[first(idx[l])]
    else:
        minus *= far[last(idx[l])]

print(cham * (field - minus))  # 계산 후 출력.
