K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

start = 1
end = max(cables)
answer = 0

while start <= end:
    mid = (start + end) // 2

    total = sum(cable // mid for cable in cables)

    if total >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)