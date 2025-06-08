N, K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

sorted_coins = sorted(coins, reverse=True)

count = i = 0

while True:
    if K >= sorted_coins[i]:
        K -= sorted_coins[i]
        count += 1

    else:
        i += 1

    if K == 0: break

print(count)
