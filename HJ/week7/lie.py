### 백준 1043 - 거짓말

'''
4 3
0
2 1 2
1 3
3 2 3 4

5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5

'''

N, M = map(int, input().split()) # 사람수, 파티수
people= list(map(int, input().split())) # 아는사람

if people[0] == 0 :
    print(M)
    exit()
else :
    people = people[1:]

party = []
for m in range(M) :
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])

# 거짓말 아는 사람 추출
change= True
while change :
    change = False
    for now in party :
        if any(person in people for person in now):
            ## 지피티 도움 부분 : for문 한번 더 안써도 되게 함
            for p in now:
                if p not in people:
                    people.append(p)
                    change= True


# 파티 개수 추출
cnt = M
for now in party :
    for person in people :
        if person in now :
            cnt -= 1
            break
print(cnt)
