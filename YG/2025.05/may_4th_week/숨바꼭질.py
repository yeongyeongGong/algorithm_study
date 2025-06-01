# 걷거나 순간이동을 할 수 있음
# 현재위치 +- 1 or 현재위치 * 2
# 해당 좌표가 현재위치와 인접한 노드라는 의미
# 시작위치와 도착위치가 주어졌을 때 찾을 수 있는 가장 빠른 시간
from collections import deque

N, K = map(int, input().split())    # N: 수빈이 위치(시작위치), K: 동생위치(도착위치)
cnt = 0
q = deque()
q.append((N,cnt))
visit = [0] * 100001
visit[N] = 1
while q:   # 수빈이가 동생을 찾으면 break
    N, cnt = q.popleft()

    if N == K:
        print(cnt)
        break
    if 0 <=N-1 <=100000:
        if not visit[N-1]:
            q.append((N-1,cnt+1))
            visit[N-1] = 1
    if 0 <=N+1<=100000:
        if not visit[N+1]:
            q.append((N+1,cnt+1))
            visit[N+1] = 1
    if 0 <=2*N <= 100000:
        if not visit[N*2]:
            q.append((N*2,cnt+1))
            visit[2*N] = 1

    # 아래 12줄은 4줄로 줄일 수 있음,,,바보다,,,

    # for next_pos in (now - 1, now + 1, now * 2):
    #     if 0 <= next_pos <= 100000 and not visit[next_pos]:
    #         visit[next_pos] = 1
    #         q.append((next_pos, cnt + 1))