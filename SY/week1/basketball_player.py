N = int(input())

names = []
for _ in range(N):
    names.append(input())

alpha = []
for name in names:
    if name[0] not in alpha:
        alpha.append(name[0])

alpha.sort()

cnt = [0] * len(alpha)
for i in range(len(alpha)):
    for name in names:
        if alpha[i] == name[0]:
            cnt[i] += 1

impossible = True

for i in range(len(cnt)):
    if cnt[i] >= 5:
        print(alpha[i], end='')
        impossible = False

if impossible:
    print('PREDAJA')