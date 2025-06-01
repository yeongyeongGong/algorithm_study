## 백준 - 촌수계산
def dfs(start, end, cnt =0 ):
    visited[start] = 1

    if start == end :
        return cnt

    for node in lst[start]:
        if visited[node] == 0:
            temp = dfs(node, end, cnt +1)
            if temp != -1:
                return temp
    return -1

N = int(input())
lst = [[] for _ in range(N+1)]

s, e = map(int, input().split())

M = int(input())
for m in range(M):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visited= [0] * (N+1)

result=dfs(s,e)
print(result)
