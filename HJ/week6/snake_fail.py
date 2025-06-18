### 백준 10875 - 뱀
## 실패.. 메모리초과 계쏙 뜸
# 지피티랑 싸워서 물어봤더니 선분만 저장하는 형식으로 해야한다고 함
# 근데 얘 코드도 런타임 오류떠서 걍 포기..

'''
3
4
2 L
2 L
1 L
5 R

'''

L = int(input())
N = int(input())
if N == 0 :
    print(4)
    exit()
#arr= [[0] * (2*L +1) for _ in range(2*L +1)]
visited= set()

now_dir = [0,1] # 기본 오른쪽으로 이동
# arr[L][L] = 1
now = (L,L)
visited.add(now)
left = [[0,1],[-1,0],[0,-1],[1,0]]
right = [[0,1],[1,0],[0,-1],[-1,0]]
cnt = 0
for n in range(N) :
    num, dir = input().split()
    num = int(num)
    while num > 0 :
        cnt += 1
        num -= 1
        x = now[0]+now_dir[0]
        y = now[1]+now_dir[1]
        if x < 0 or y < 0 or x > (2*L) or y > (2*L) or (x,y) in visited :
            print(cnt)
            exit()
        visited.add((x,y))
        now = (x,y)
    if dir == 'L' :
        idx = left.index(now_dir)
        new_idx = (idx + 1) % 4
        now_dir = left[new_idx]
    elif dir == 'R' :
        idx = right.index(now_dir)
        new_idx = (idx + 1) % 4
        now_dir = right[new_idx]


print(cnt)