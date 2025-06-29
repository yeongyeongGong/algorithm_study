# R x C 직사각형 격자판
# 비어있거나 폭탄
# 폭탄이 있는칸은 3초 후에 폭발
# 폭탄이 있던 칸 + 인접 4칸(상하좌우) 파괴
# 인접칸(상하좌우)에 폭탄이 있었다면 폭발없이 그냥 폭탄만 파괴됨
# 즉 연쇄반응 x
# 첫 턴에 폭탄 설치
# 두번째 턴에 아무것도 안함
# 3번째 턴에 폭탄이 안 설치 된 곳에 폭탄 설치
# 다음턴에 3초가 지났으므로 첫턴에 설치한 폭탄 터짐
# 위와같은 패턴이 반복되고 N초 후의 격자 상태를 구하여라

R, C, N = map(int, input().split()) # R : 세로, C : 가로, N : 몇 초뒤의 상태(?)
boom_map = [list(input()) for _ in range(R)]

if N == 1:
    for row in boom_map:
        print(*row, sep='')

    exit()


time = 2
# 첫턴에 설치하는 폭탄
for i in range(R):
    for j in range(C):
        if boom_map[i][j] == '.':
            boom_map[i][j] = str(time)
        else:
            boom_map[i][j] = '0'

r=[1,-1,0,0]
c=[0,0,1,-1]

while time != N:

    time += 1
    for i in range(R):
        for j in range(C):

            if boom_map[i][j] == '.':
                continue
            elif time - 3 >= int(boom_map[i][j]):
                temp =int(boom_map[i][j])
                boom_map[i][j] = '.'
                for k in range(4):
                    ri = i + r[k]
                    cj = j + c[k]
                    if 0<=ri<=R-1 and 0<=cj<=C-1:
                        if boom_map[ri][cj] != '.':
                            if temp == int(boom_map[ri][cj]):
                                continue
                            else:
                                boom_map[ri][cj] = '.'



    if time != N:
        time += 1
        for i in range(R):
            for j in range(C):
                if boom_map[i][j] == '.':
                    boom_map[i][j] = str(time)    # 폭탄 설치할 때 시간 기록해줌
    else:
        break

for i in range(R):      # 폭탄 안터진곳은 다 O로 바꿔주기
    for j in range(C):
        if boom_map[i][j] != '.':
            boom_map[i][j] = 'O'

for row in boom_map:
    print(*row, sep='')