# 사람들의 번호는 1부터
# 진실 or 과장
# 진실을 아는사람이 한명이라도 있으면 그 파티에서 과장 X
# 거짓말 몇번 할 수 있는지 구하기

N,M = map(int, input().split()) #N: 사람의 수 , M: 파티의 수
know_true = list(map(int, input().split())) # 진실을 아는 사람의 수와 그의 번호
know_true.pop(0)    # 사람수는 리스트에서 없앰
party = []

cnt = 0

for _ in range(M):
    people = list(map(int, input().split()))
    people.pop(0)   # 사람수는 리스트에서 없앰
    party.append(people)
x=0
# 진실을 아는 인원을 가려내고
while x < M:
    for i in range(M):
        know_cnt = 0
        for j in range(len(party[i])):  # 지금 이 파티 참석 인원이 아는사람 리스트에 있으면
            if party[i][j] in know_true:
                know_cnt += 1   # 현재 파티의 아는사람 인원 +1
                know_true.extend(party[i])  # 현재 파티인원 모두 진실을 아는 사람 리스트에 추가
                continue
    x += 1

# 위와 동일한 작업으로 거짓말 가능 여부 확인
for i in range(M):
    know_cnt = 0
    for j in range(len(party[i])):  # 지금 이 파티 참석 인원이 아는사람 리스트에 있으면
        if party[i][j] in know_true:
            know_cnt += 1  # 현재 파티의 아는사람 인원 +1
            continue

    if know_cnt == 0 :  # 현재 파티에 진실을 아는 사람이 하나도 없으면
        cnt += 1    # 거짓말 횟수 +1
print(cnt)


