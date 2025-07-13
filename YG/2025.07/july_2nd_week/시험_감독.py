N = int(input())    #  시험장 개수

people = list(map(int, input().split()))    # 각 시험장 응시자 수
B,C =  map(int, input().split())    # B: 총감독관 감시 수, C: 부감독관 감시 수
cnt = 0
for i in range(N):
    if people[i] <= B:
        cnt += 1
    elif people[i] <= C:    # 한 강의실에 총감독관은 무조건 들어강야함
        cnt += 2
    elif people[i] > B and people[i] > C:
        cnt += 1
        people[i] -= B
        cnt += (people[i] // C)
        if people[i] % C != 0:
            cnt += 1

print(cnt)