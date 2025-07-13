# 거짓말

def bfs(x):
    queue = [x]

    while queue:
        cur = queue.pop(0)
        people[cur] = 1

        for i in range(M):
            if cur in members[i]:
                for j in range(len(members[i])):
                    if not people[members[i][j]]:
                        queue.append(members[i][j])
                        truth.append(members[i][j])
                        people[members[i][j]] = 1

    return

N, M = map(int, input().split())

truth = list(map(int, input().split()))
truth_len = truth.pop(0)

members = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    members[i].pop(0)

cnt = 0

people = [0] * (N + 1)

for i in range(truth_len):
    bfs(truth[i])

for k in range(M):
    for l in members[k]:
        if l in truth:
            break
    else:
        cnt += 1

print(cnt)
