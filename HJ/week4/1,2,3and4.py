### 백준 - 1,2,3 더하기 4

'''

3
4
7
10

'''

T = int(input())
for t in range(T):
    n = int(input())
    max_3 = n // 3
    cnt = 0

    while max_3 >= 0 :
        tmp = n - max_3 * 3
        max_2 = tmp // 2
        cnt += 1
        cnt += max_2
        # while max_2 >= 0 :
        #     max_1 = tmp - max_2 *2
        #     cnt += 1
        #     # print(max_3, max_2, max_1)
        #     max_2 -= 1
        max_3 -= 1

    print(cnt)
