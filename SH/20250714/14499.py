# 주사위 굴리기

N, M, x, y, K = map(int, input().split())

# 주사위 모양 설정. b: 바닥, d: 위.
die = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}

# 동서남북 델타.
delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

field = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

for i in range(K):
    # 현재 위치를 기반으로 움직일 위치를 설정.
    nr, nc = x + delta[order[i]][0], y + delta[order[i]][1]

    # 범위 내라면 진행, 범위 밖이라면 아무것도 하지 않음.
    if 0 <= nr < N and 0 <= nc < M:

        # 각 방향에 따라 주사위 포지션을 변경.
        # 동쪽으로 굴린다면 e, b, f, d 가 한 칸씩 우측으로 밀린다.
        if order[i] == 1:
            die['e'], die['b'], die['f'], die['d'] = die['d'], die['e'], die['b'], die['f']
        
        # 서쪽으로 굴린다면 e, b, f, d 가 한 칸씩 좌측으로 밀린다.
        elif order[i] == 2:
            die['e'], die['b'], die['f'], die['d'] = die['b'], die['f'], die['d'], die['e']
        
        # 북쪽으로 굴린다면 a, b, c, d 가 한 칸씩 위쪽으로 밀린다.
        elif order[i] == 3:
            die['a'], die['b'], die['c'], die['d'] = die['b'], die['c'], die['d'], die['a']
        
        # 남쪽으로 굴린다면 a, b, c, d 가 한 칸씩 아래쪽으로 밀린다.
        else:
            die['a'], die['b'], die['c'], die['d'] = die['d'], die['a'], die['b'], die['c']
        
        # 밀리고 난 후에 바닥 숫자를 판별.
        # 바닥에 숫자가 있다면 그 숫자를 주사위에 복사하고 바닥 숫자는 지운다.
        if field[nr][nc]:
            die['d'] = field[nr][nc]
            field[nr][nc] = 0
        
        # 바닥에 0이 있다면 주사위의 숫자를 바닥에 복사한다.
        else:
            field[nr][nc] = die['d']
        
        # 위쪽 면의 숫자를 print.
        print(die['b'])

        # 현재 위치를 이동한 위치로 변경.
        x, y = nr, nc