numbers = []
sum_n = 0
for _ in range(5):
    n = int(input())
    numbers.append(n)
    sum_n += n

# 평균구하기
avg = int(sum_n / 5)

# 중앙값 구하기
for i in range(5):
    for j in range(i, 5):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
mid = numbers[2]

print(avg)
print(mid)
