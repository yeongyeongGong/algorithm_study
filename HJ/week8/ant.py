### 백준 3048 - 개미

'''
3 3
ABC
DEF
0

3 3
ABC
DEF
1

'''

n1, n2 = map(int, input().split())
arr1 = list(input().strip())[::-1] # 오른쪽
arr2 = list(input().strip()) # 왼쪽
now = arr1 + arr2

cnt = int(input())
if cnt == 0 :
    print(''.join(now))
    exit()

while cnt :
    i = 0
    while i < n1+n2-1 :
        if (now[i] in arr1 and now[i+1] in arr2):
            now[i], now[i+1] = now[i+1], now[i]
            i += 2
            continue
        i += 1
    cnt -= 1
    # print(now)

print(''.join(now))

