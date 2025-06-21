n = int(input())

arr = []
for i in range(1,n+1):
    arr.append(i)

# print(arr)
lst = list(map(int,input().split()))

bbada = []
for j in range(n):
    if arr[j] != lst[j]:
        bbada.append(lst[j])

# print(bbada)

cnt = 0
for k in bbada:
    cnt += 1

print(cnt)