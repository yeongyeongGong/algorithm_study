n = int(input())
customer = map(int, input().split())

pc = [0]*101

cnt = 0

for i in customer:
    if pc[i] == 0: #빈 자리라면
        pc[i] = 1

    else:
        cnt += 1

print(cnt)