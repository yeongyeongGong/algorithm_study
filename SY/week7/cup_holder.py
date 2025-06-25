N = int(input())
seat = input()
cnt = 1
i = 0
while i < len(seat):
    if seat[i] == 'S':
        cnt += 1
        i += 1

    elif seat[i] == 'L':
        cnt += 1
        i += 2

if cnt >= N:
    cnt = N

print(cnt)