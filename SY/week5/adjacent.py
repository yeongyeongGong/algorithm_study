def solution(board, h, w):
    n = len(board)
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    color = board[h][w]
    cnt = 0

    for r, c in directions:
        nr = h + r
        nc = w + c

        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == color:
            cnt += 1

    answer = cnt
    return answer


if __name__ == "__main__":
    board = [list(map(input().split()))]
    h, w = map(int, input().split())
    print(solution(board, h, w))