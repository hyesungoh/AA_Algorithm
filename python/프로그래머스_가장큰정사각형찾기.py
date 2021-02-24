def solution(board):
    ylen = len(board)
    xlen = len(board[0])
    ans = 1 if board[0][0] else 0

    for y in range(1, ylen):
        for x in range(1, xlen):
            if not board[y][x]:
                continue

            up = board[y-1][x]
            down = board[y][x-1]
            diag = board[y-1][x-1]
            if up > 0 and down > 0 and diag > 0:
                board[y][x] = min(up, down, diag) + 1
                ans = max(ans, board[y][x])

    return ans * ans
