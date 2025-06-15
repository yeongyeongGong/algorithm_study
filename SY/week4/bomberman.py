dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def find_bomb(R, C, map):
    bomb_idx = []
    for row in range(R):
        for col in range(C):
            if map[row][col] == 'O':
                bomb_idx.append((row, col))

    return bomb_idx

def bomberman(R, C, map):
    for r in range(R):
        for c in range(C):
            if map[r][c] == '.':
                map[r][c] = 'O'
    return map

R, C, N = map(int, input().split())

map = [list(input().rstrip())  for _ in range(R)]

if N == 1:
    for row in map:
        print(''.join(row))
    exit()

bomb = find_bomb(R, C, map)
for time in range(2, N+1):
    if time%2 == 0:
        new_map = bomberman(R, C, map)
    else:
        for r, c in bomb:
            new_map[r][c] = '.'
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if 0 <= nr < R and 0 <= nc < C:
                    new_map[nr][nc] = '.'

        bomb = find_bomb(R, C, new_map)

for row in new_map:
    print(''.join(row))