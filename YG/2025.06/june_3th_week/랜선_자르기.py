K,N = map(int, input().split())  #K: 소지 랜선개수, N: 나눠야하느 랜선개수
cable = []
for _ in range(K):
    length = int(input())
    cable.append(length)

start = 1
end = max(cable)
result = 0  # 가능한 최대 길이

while start <= end:
    mid = (start + end) // 2  # 자를 길이
    count = sum(x // mid for x in cable)  # 자른 조각 수 계산

    if count >= N:
        result = mid  # 가능한 길이 저장
        start = mid + 1
    else:
        end = mid - 1

print(result)
