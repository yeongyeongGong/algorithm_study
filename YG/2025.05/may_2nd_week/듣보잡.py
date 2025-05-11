N, M = map(int, input().split()) #N: 듣도 못한 사람 수 , M : 보도못한 사람 수
people = {}
not_listen_not_look = []
for _ in range(N+M):
    name = input()
    if name not in people: # 키값으로 없으면 이름 추가
        people[name] = 1
    else:   # 있는데 한번 더 나온거면 듣도보도 못한 명단에 추가
        not_listen_not_look.append(name)
not_listen_not_look.sort()

print(len(not_listen_not_look))
for i in not_listen_not_look:
    print(i)
