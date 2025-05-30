n = int(input())

for i in range(n):
    lst = list(map(int,input().split()))

    even_num = []
    for j in range(len(lst)):
        if lst[j]%2 == 0:
            even_num.append(lst[j])

    even_num.sort()

    #덧셈
    sum_num = 0
    for k in range(len(even_num)):
        sum_num += even_num[k]

    print(sum_num, even_num[0])

