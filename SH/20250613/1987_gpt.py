# 알파벳

# idea
# 1. 비트 마스크
    # A = 1 << 1, B = 1 << 2, C = 1 << 3 ... 식으로 생각해서
    # 26자리의 이진수와 각 알파벳을 비교하는 방법.
# 2. 가지치기
    # 알파벳의 최대 갯수가 26개이므로, 길이가 26이 되면 자동 종료.
# 3. 위치의 이동
    # 해당 위치에 갔는지, 가지 않았는지를 표현하기 위해 비트 마스크를 각 위치에 저장하며 이동.

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동남서북


def dfs(x, y, z, l):
    stack = []
    char = ord(field[x][y]) - ord('A')  # 비트 마스크 사용. 첫 알파벳을 숫자로 바꾸고,
    mask = 1 << char  # 이진수로 변환.
    stack.append((x, y, mask, l))  # r, c, 비트 마스크, 길이를 저장.
    cnt_max = 1

    while stack:
        cr, cc, path, cnt = stack.pop()

        if cnt == 26:  # 가지치기.
            return cnt

        if cnt_max < cnt:  # 최대 길이를 갱신.
            cnt_max = cnt

        for i in range(4):  # 4방향을 확인하면서
            nr, nc = cr + delta[i][0], cc + delta[i][1]
            if 0 <= nr < R and 0 <= nc < C:
                ch = ord(field[nr][nc]) - ord('A')  # 해당 위치 알파벳을 숫자로 바꾸고,
                if not (path & (1 << ch)):  # 이진수로 변환하여 비트 마스크와 비교.
                    stack.append((nr, nc, path | (1 << ch), cnt + 1))  # 없으면 비트 마스크에 추가.

    return cnt_max

R, C = map(int, input().split())

field = [list(input()) for _ in range(R)]

result = dfs(0, 0, field[0][0], 1)

print(result)
