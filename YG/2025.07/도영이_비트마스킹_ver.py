N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

min_val = float('inf')

# 1부터 2^N - 1까지 모든 조합 (공집합 제외)
for bit in range(1, 1 << N):
    sour = 1
    bitter = 0
    for i in range(N):
        if bit & (1 << i):  # i번째 재료를 선택했으면
            s, b = ingredients[i]
            sour *= s
            bitter += b
    min_val = min(min_val, abs(sour - bitter))

print(min_val)
