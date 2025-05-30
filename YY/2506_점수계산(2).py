n = int(input())

num = list(map(int,input().split()))
# print(num)

score = 0
consecutive = 0

for i in num:
    if i == 1: #1이라면
        consecutive += 1
        score += consecutive

    if i == 0 :
        consecutive = 0 #초기화

print(score)