N, M = map(int, input().split())
truth_input = list(map(int, input().split()))
truth_knowers = truth_input[1:]  # 진실 아는 사람들만 추출

graph_person = [[] for _ in range(N + 1)]  # 1~N 사람 기준
graph_party = [[] for _ in range(M)]       # 0~M-1 파티 기준
visited_person = [False] * (N + 1)
visited_party = [False] * M

# 파티 정보 입력 + 그래프 구성
for i in range(M):
    data = list(map(int, input().split()))
    people = data[1:]
    graph_party[i] = people
    for person in people:
        graph_person[person].append(i)  # 사람이 속한 파티 추가

# BFS로 진실 전파
queue = []

for person in truth_knowers:
    queue.append(person)
    visited_person[person] = True

while queue:
    current = queue.pop(0)
    # current 사람이 참석한 파티들 확인
    for party in graph_person[current]:
        if not visited_party[party]:
            visited_party[party] = True  # 이 파티는 진실에 오염됨
            # 이 파티에 있는 사람들 중 아직 방문 안 한 사람 큐에 추가
            for next_person in graph_party[party]:
                if not visited_person[next_person]:
                    visited_person[next_person] = True
                    queue.append(next_person)

# 진실 전파되지 않은 파티 개수 세기
answer = 0
for i in range(M):
    if not visited_party[i]:
        answer += 1

print(answer)
