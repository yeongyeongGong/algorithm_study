dice = list(map(int, input().split()))
count = [0] * 7

for d in dice:
    count[d] += 1

result = 0
max_die = 0
for i in range(1, 7):
    # count[i]가 3인 경우
    if count[i] == 3:
        result = 10000 + i * 1000
    # count[i]가 2인 경우
    elif count[i] == 2:
        result = 1000 + i * 100
    # count[i]가 1인 경우
    elif count[i] == 1:
        if max_die < i:
            max_die = i

if not result:
    print(100 * max_die)
else:
    print(result)