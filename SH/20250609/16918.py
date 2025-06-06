# 봄버맨

# idea
# 짝수 초 마다는 필드가 새로 정렬이 되고,
# 홀수 초 마다는 폭탄이 터진다.
# 하지만, 1초에서의 필드와 5초에서의 필드는 다를 수 있다.

delta = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]  # 자신, 동, 남, 서, 북

R, C, N = map(int, input().split())  # 행, 열, 초

field_1 = [list(input()) for _ in range(R)]  # 시작, 1초
field_2 = [['O'] * C for _ in range(R)]  # 2초, 4초
field_3 = [['O'] * C for _ in range(R)]  # 3초
field_4 = [['O'] * C for _ in range(R)]  # 5초

for r in range(R):  # 3초에서의 필드 변화
    for c in range(C):
        if field_1[r][c] == 'O':
            for d in range(5):
                nr, nc = r + delta[d][0], c + delta[d][1]
                if 0 <= nr < R and 0 <= nc < C:
                    field_3[nr][nc] = '.'

for r in range(R):  # 5초에서의 필드 변화
    for c in range(C):
        if field_3[r][c] == 'O':
            for d in range(5):
                nr, nc = r + delta[d][0], c + delta[d][1]
                if 0 <= nr < R and 0 <= nc < C:
                    field_4[nr][nc] = '.'

if N in {0, 1}:  # 0초, 1초일 때는 초기 세팅된 필드 출력.
    for r in range(R):
        for c in range(C):
            print(field_1[r][c], end='')
        print()
elif not N % 2:  # 짝수 초에는 새로 정렬한 필드 출력.
    for r in range(R):
        for c in range(C):
            print(field_2[r][c], end='')
        print()
elif N % 4 == 3:  # 3초, 7초, 11초... 에는 3초 필드 출력.
    for r in range(R):
        for c in range(C):
            print(field_3[r][c], end='')
        print()
else:  # 5초, 9초, 13초... 에는 5초 필드 출력.
    for r in range(R):
        for c in range(C):
            print(field_4[r][c], end='')
        print()
