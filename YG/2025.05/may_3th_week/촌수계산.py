# 촌수 계산 문제
# 직계자식 1촌 조부와 손자관계 2촌 그외의 한그래프 내에서의 관계는 3촌

N = int(input())    # 전체 사람의 수
A,B = map(int, input().split()) # A와 B의 촌수를 구해야함
M = int(input())    # 부모 자식 간의 관계의 개수 (간선 수)

family = [[] for _ in range(N + 1)]

for _ in range(M):
    X,Y = map(int, input().split()) # x는 y의 부모
    family[X].append(Y)     # 인접 정보 저장
    family[Y].append(X)
# print(family)

visited = [0] * (N+1)
stack = [(A,0)]
visited[A] = 1
now, cnt = A,0  # now = 현재 노드 위치, cnt = 촌수

while stack:
    now,cnt = stack.pop()
    if now == B:
        break

    for i in family[now]:
        if visited[i] == 0 :
            visited[i] = 1
            stack.append((i,cnt+1))

    # 처음엔 cnt를 별도로 저장하고 +를 해줬더니 모든 노드를 들릴 때마다 +1 을 해줘서 촌수가 비정상적으로 크게나옴

    # cnt +=1

if now != B:
    print(-1)
else:
    print(cnt)
