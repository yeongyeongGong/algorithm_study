### 백준 1654 - 랜선 자르기
'''
4 11
802
743
457
539

5 5
500
500
500
500
50005

계속 시간초과 뜸
정선적인 해결방법은 이진탐색!
근데 이거 너무 아까워서 그냥 이대로 제출해용

'''
import math

K, N = map(int, input().split())

lines = []
for k in range(K) :
    lines.append(int(input()))

length = sum(lines) // N

while length > 0 :
    cnt = 0
    max_remain = 0
    mok=0
    for l in lines :
        if l < length :
            continue
        cnt += l // length
        if l % length > max_remain :
            max_remain = l % length
            mok = l // length

    if cnt >= N :
        print(length)
        break

    if mok == 0 :
        length -= 1
    else :
        dec = math.ceil((length-max_remain) / mok )
        if dec < 1 :
            dec = 1
        length -= dec

