### 백준 - 듣보잡

N, M = map(int, input().split())
a,b = set(), set()
for n in range(N):
    a.add(input())
for m in range(M):
    b.add(input())

result = list(a&b)
result.sort()

print(len(result))
for r in result:
    print(r)