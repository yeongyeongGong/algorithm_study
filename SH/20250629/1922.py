# 네트워크 연결

# kruskal

def find(x):  # 대표자를 찾는 함수.
    if x == head[x]:  # 대표가 본인이라면 본인 반환.
        return x
    else:  # 대표가 본인이 아니라면 대표를 찾으러 감.
        return find(head[x])

def union(x, y):  # 같은 덩어리로 묶는 함수.
    global head
    if find(x) != find(y):  # 대표가 서로 다르면
        head[find(x)] = y  # 대표를 갖게 하고
        return True  # True 반환.
    else:
        return False  # 대표가 같다면 False 반환.


N = int(input()) + 1
M = int(input())

head = [i for i in range(N)]  # 대표를 표시하는 list.
count = 0  # 연결 갯수.
cost = 0  # 연결 비용.

network = [list(map(int, input().split())) for _ in range(M)]

network.sort(key=lambda x:x[2])  # 정보를 받아 가격 순으로 정렬.

for i in range(M):  # 모든 가격을 보는데,
    if count == N - 2:  # 연결 갯수가 충족되면 break.
        break

    # 서로 이어지지 않았다면(대표가 다르면) 잇고 비용 추가.
    if union(network[i][0], network[i][1]):
        cost += network[i][2]
        count += 1

print(cost)  # 출력.


# prim

# N = int(input()) + 1
# M = int(input())
#
# network = [list(map(int, input().split())) for _ in range(M)]
# cost = 0
#
# for i in range(1, N - 1):  # 모든 노드를 돌면서
#
#     cheap = 10001  # 최소 비용을 찾음.
#
#     for j in range(M):  # 모든 연결 정보를 탐색해서
#         if network[j][0] == i:  # 해당 노드의 연결 정보라면
#             if cheap > network[j][2]:
#                 cheap = network[j][2]  # 싼 값을 저장.
#     cost += cheap  # 비용 추가.
#
# print(cost)  # 출력.
