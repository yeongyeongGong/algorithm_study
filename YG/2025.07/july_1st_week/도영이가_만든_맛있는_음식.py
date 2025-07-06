# 가지고있는 재료로 만들 수 있는 모든 조합을 구해서
# 쓴맛과 신맛의 차이 최소값 구하기

N = int(input())    # 재료의 수
ingredients = [tuple(map(int, input().split())) for _ in range(N)]   # 재료들의 신맛과 쓴맛을 튜플로 저장

min_val = 0xffffffff

for i in range(1, N+1): # 재료가 1~N개인 모든 조합
    stack = []
    stack.append((0, []))  # (시작 인덱스, 현재 조합)

    while stack:
        index, selected = stack.pop()


        if len(selected) == i: # 조합이 i개가 되면 신맛 쓴맛 계산
            sour = 1
            bitter = 0
            for j in selected:
                s, b = ingredients[j]
                sour *= s
                bitter += b
            min_val = min(min_val, abs(sour - bitter))
            continue

        # 추가 조합
        for k in range(index, N):
            stack.append((k + 1, selected + [k]))

print(min_val)
