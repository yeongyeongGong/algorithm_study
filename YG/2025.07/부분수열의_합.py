N, S = map(int,input().split())
arr = list(map(int, input().split()))

cnt = 0

for i in range(1, N+1):
    stack = []
    stack.append((0,[]))

    while stack:
        index, selected = stack.pop()

        if len(selected) == i:
            if sum(selected) == S:
                cnt += 1
            continue

        for j in range(index, N):
            stack.append((j+1, selected + [arr[j]]))  # 값 자체를 넣음

print(cnt)
