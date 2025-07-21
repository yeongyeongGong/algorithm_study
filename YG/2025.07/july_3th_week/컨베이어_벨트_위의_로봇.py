from collections import deque
N,K = map(int, input().split()) #N: 컨베이어벨트 칸, K: 정지해야하는 갯수

durability = deque(map(int, input().split()))   # 내구도

robots = deque([False] * N)

step = 0
zero_count = 0
while zero_count < K:

    step += 1   # 매번 회전
    durability.rotate(1)
    robots.rotate(1)
    robots[N - 1] = False   # 회전 후 로봇이 내리는 위치에 있으면 로봇 하차

    # 앞에서부터 보게되면 로봇 이동과정에서 충돌이 생김
    for i in range(N-2,-1,-1):  # 로봇이 내리는 위치 => N-1 -> 이동하기 전의 로봇위치를 봐야하니까 N-2부터 봐야함
        if robots[i] and not robots[i+1] and durability[i+1] >0:
            robots[i+1] = True
            robots[i] = False
            durability[i+1] -= 1
            if durability[i + 1] == 0:
                zero_count += 1
    robots[N - 1] = False  # 이동 후에도 하차 위치 로봇 내리기

    if not robots[0] and durability[0] > 0: # 로봇이 승차 위치에 아직 없고, 내구도가 1 이상이면
        durability[0] -= 1  # 로봇 태우고, 내구도 1 깎기
        robots[0] = True
        if durability[0] == 0:
            zero_count += 1
    if robots[N-1]: # 로봇이 하차위치에 도착하면 하차시키기
        robots[N-1] = False

    # if durability.count(0) == K:    # 내구도 0의 갯수가 K와 동일해지면 작업 멈추기
    #     break

print(step)




