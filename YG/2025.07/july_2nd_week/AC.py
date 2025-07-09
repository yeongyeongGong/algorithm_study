# R:수의 순서 뒤집기, D: 첫 번째 수를 버리기
# 배열이 비어있는 상태로 D를 쓰면 오류 발생
from collections import deque

T = int(input())
for _ in range(T):
    p = list(input()) # p -> 수행할 함수
    n = int(input())    # n -> 배열에 들어있는 수의 개수
    arr = deque(input().strip('[]').split(',')) # [x1,x2,x3 ...,xn]

    if arr[0] == '':    # 빈배열일때
        if 'D' in p: # 수행할 작업에 D가있으면
            print('error')
        else:   # R만 있으면 그냥 빈배열
            print('[]')
        continue

    # flag 변수 선언
    reverse_flag = False
    error_flag = False

    for i in range(len(p)):
        if p[i] == 'R':
            reverse_flag = not reverse_flag
        elif p[i] == 'D':
            if len(arr) == 0:
                print('error')
                error_flag = not error_flag
                break
            else:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
    if reverse_flag:
        arr.reverse()
    if len(arr) != 0 :
        print('[', end='')
        print(','.join(map(str, arr)), end='')
        print(']')
    elif not error_flag:
        print('[]')

