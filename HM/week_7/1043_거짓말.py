# N : 사람 수, M : 파티 수
N, M = map(int, input().split())

# true_people : 진실을 아는 사람들(번호)
n, *true_people = map(int, input().split())

party = []

# 1. 진실을 알고 있는 사람이 속한 파티는 무조건 제외
# 2. 위 파티에 다른 사람도 있을 시 그 사람도 진실을 듣기에 진실을 들은 사람이 속한 다른 파티도 제외(진실이 전파됨)

for _ in range(M):
    # count : 파티에 참가한 사람 수, people : 파티에 참석한 사람 번호
    count, *people = map(int, input().split())
    party.append((count, people))


# 진실 전파가 끝날때까지 반복
changed = True
while changed:
    changed = False
    for people in party:
        # 현재 파티에 true_people 중 한명이라도 있으면
        if any(p in true_people for p in people[1]):
            for p in people[1]:
                # 파티원 중 true_people에 속하지 않은 사람 추가(진실이 전파됨)
                if p not in true_people:
                    true_people.append(p)
                    # 아직 진실이 전파될 가능성이 있으므로 changed를 True로 설정해서 다시 반복
                    changed = True
# print(true_people)
result = 0
for p in party:
    for i in p[1]:
        # 파티에 진실을 아는 사람이 한명이라도 있으면 반복문 탈출
        if i in true_people:
            break
    # 파티에 진실을 아는 사람이 없으면 1 추가
    else:
        result += 1

print(result)