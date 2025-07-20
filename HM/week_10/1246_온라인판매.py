N, M = map(int, input().split())
P = []
for _ in range(M):
    price = int(input())
    P.append(price)

# 브루트 포스?
max_price = 0
low_egg_price = 0xffffff

for A in P:
    customer = 0
    for p in P:
        if A <= p:
            customer += 1
            if customer == N:
                break
    total = customer * A
    if max_price < total:
        max_price = total
        low_egg_price = A
    elif max_price == total:
        if low_egg_price > A:
            low_egg_price = A

print(low_egg_price, max_price)