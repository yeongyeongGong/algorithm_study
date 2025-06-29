T = int(input())
for _ in range(T):
    N = int(input())
    wear_dict = {}
    for _ in range(N):
        wear, category = input().split()
        wear_dict.setdefault(category, []).append(wear)
    # 카테고리별로 안 입거나 입는 경우의 수 존재
    # 모든 옷을 안 입을 수는 없음
    result = 1
    for clothes in wear_dict.values():
        # 입는 경우(len(clothes)) + 안 입는 경우(1)
        result *= (len(clothes) + 1)

    # 모든 옷을 안 입는 경우는 제외
    print(result - 1)
