N = int(input())
time = list(map(int, input().split()))
time.sort()

sum_time = 0


for i in range(1,N+1):
    for j in range(i):
        sum_time += time[j]


print(sum_time)

