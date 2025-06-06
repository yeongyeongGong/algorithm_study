# 별 찍기 - 18

# 각 삼각형 밑변의 index 를 구하는 함수
def dp(x):
    if x == 1:
        return [0]
    arr = dp(x - 1)
    if len(arr) % 2:
        for i in range(len(arr)):
            arr[i] += 1
        new_arr = [0] + arr
    else:
        for i in range(len(arr)):
            arr[i] += (width[x - 1] + 1) // 2
        new_arr = [width[x - 1] + 1] + arr
    return new_arr


n = int(input())
# 높이는 2 ** i - 1 로 일반화할 수 있는데, 삼각형 방향에 따라 양수, 음수를 다르게 설정.
height = [(2 ** i - 1) * ((-1) ** (i + 1)) for i in range(n + 1)]
width = [0] * (n + 1)
width[1] = 1

# 밑변의 길이는 (i - 1) + 2 * i 로 일반화할 수 있다.
for i in range(2, n + 1):
    width[i] = width[i - 1] + 2 ** i

# field 설정. height[-1] 이 음수가 될 수 있으므로 절대값을 씌운다. 이후로도.
field = [[' '] * width[-1] for _ in range(abs(height[-1]))]

# 삼각형의 밑변 index 를 구해 리스트로 정렬.
bottom = dp(n)

# 각 삼각형의 밑변에 먼저 * 을 적는다.
for j in range(n):
    for x in range(width[(-1 * j - 1)]):
        field[bottom[j]][x + ((width[-1] - width[(-1 * j - 1)]) // 2)] = '*'

# 이후 빗변들을 그린다. 삼각형의 방향에 따라 다르게 설정.
for j in range(n, 0, -1):

    # 빗변의 시작점을 설정.
    h_key = bottom[n - j]

    # 삼각형이 거꾸로 되어있다면...
    if height[j] < 0:
        for w in range(1, width[j]):
            if w <= width[j] // 2:
                h_key += 1
                field[h_key][w + ((width[-1] - width[j]) // 2)] = '*'
            else:
                h_key -= 1
                field[h_key][w + ((width[-1] - width[j]) // 2)] = '*'

    # 삼각형이 바르게 되어있다면...
    else:
        for w in range(1, width[j]):
            if w <= width[j] // 2:
                h_key -= 1
                field[h_key][w + ((width[-1] - width[j]) // 2)] = '*'
            else:
                h_key += 1
                field[h_key][w + ((width[-1] - width[j]) // 2)] = '*'

# 프린팅. 끝쪽 빈 칸은 프린트하면 안 된다.
for d in range(abs(height[-1])):
    count = 0
    stars = field[d].count('*')
    for e in range(width[-1]):
        print(field[d][e], end='')
        if field[d][e] == '*':
            count += 1
        if count == stars:
            break
    print()
