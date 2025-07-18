### 백준 15922 - 아우으 우아으이야!!

'''
5
-5 -2
-3 0
2 5
6 10
8 12

14
'''

N = int(input())
lines=[]
for n in range(N):
    lines.append(list(map(int, input().split())))

start, end = lines[0]
merged = []
for s,e in lines[1:]:
    if s <= end :
        start = min(s,start)
        end = max(e, end)
    else :
        merged.append([start, end])
        start, end = s,e
merged.append([start, end])

cnt = 0
for ms,me in merged:
    cnt += abs(me-ms)

print(cnt)