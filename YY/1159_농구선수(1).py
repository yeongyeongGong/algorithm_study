n = int(input())

first_name = []  # 첫 글자 뜯어오기
for i in range(0, n):
    name = input()
    first_name.append(name[0])

# print(first_name)
first_name.sort()  # 알파벳 순으로 정렬
# print(first_name)

final_team = []
for i in range(0, n):
    team = []  # 첫 글자 뭐로할지 정할 리스트
    cnt = 0  # 같은 첫 글자 멤버들의 수를 세어줄거임
    team.append(first_name[i])

    for j in range(i, n):
        if team[0] == first_name[j]:
            cnt += 1 #첫 글자 같으면 +

        if cnt >= 5:
            final_team.append(team[0])
            break

# print(final_team)

if not final_team: #겹치는 사람이 5명미만이거나 아무도 없는 경우는
    print('PREDAJA')

else:
    result = list(set(final_team))
    print(''.join(sorted(set(final_team))))
