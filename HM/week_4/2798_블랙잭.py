N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_jack = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = cards[i] + cards[j] + cards[k]
            if result <= M:
                max_jack = max(max_jack, result)

print(max_jack)