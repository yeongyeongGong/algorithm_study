# 바이러스에 감염된 컴퓨터와 인접한 컴퓨터는 모두 웜바이러스에 옮게된다.
# 1번컴퓨터에 웜바이러스가 걸렸고 그와 인접한 컴퓨터
# + 그 인접한 컴퓨터와 인접한 컴퓨터의 개수를 모두 구하는 문제

N = int(input())    # 컴퓨터 개수
E = int(input())    # 간선 개수

computers = [[] for _ in range(N+1)]

for _ in range(E):
    A,B = map(int, input().split())
    computers[A].append(B)  # 각 인덱스에 맞게 인접 컴퓨터 기록
    computers[B].append(A)  # 양방향 처리,,, 중요,,,;;
virus = [0] * (N+1) # 바이러스 감염 체크(방문체크)
stack = [1] # 1번 컴퓨터부터 시작
virus[1] = 1

while stack:    # 스택이 비게되면 인접한 컴퓨터들을 모두 확인했다는 것이므로 반복문 종료
    com = stack.pop()

    for i in computers[com]:    # 감염된 컴퓨터와 인접한 컴퓨터들 파악
        if virus[i] == 0:       # 인접한 컴퓨터의 바이러스를 아직 체크 안했다면
            stack.append(i)     # 해당 컴퓨터를 스택에 넣고
            virus[i] = 1        # 바이러스 체크

print(virus.count(1) - 1)   # 1번 컴퓨터는 빼고 세야함,,!!