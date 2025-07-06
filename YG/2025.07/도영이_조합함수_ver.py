from itertools import combinations

N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

min_val = float('inf')

# 재료를 1개부터 N개까지 조합해서 확인
for r in range(1, N + 1):
    for comb in combinations(ingredients, r):
        sour = 1
        bitter = 0
        for s, b in comb:
            sour *= s
            bitter += b
        min_val = min(min_val, abs(sour - bitter))

print(min_val)
