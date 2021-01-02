import sys
input = sys.stdin.readline

y, x = map(int, input().split())
board =["" for _ in range(y)]
ans = y * x

for i in range(y):
    board[i] = input()

def check_diff(sy, ey, sx, ex):
    global ans
    diff_white = [0 for _ in range(y)]
    diff_black = [0 for _ in range(y)]

    for i in range(sy, ey):
        cnt_white = 0
        cnt_black = 0
        for j in range(sx, ex):
            if (i + j) % 2 == 0:
                if board[i][j] == "W":
                    cnt_black += 1
                else:
                    cnt_white += 1
            else:
                if board[i][j] == "B":
                    cnt_black += 1
                else:
                    cnt_white += 1

        diff_black[i] = cnt_black
        diff_white[i] = cnt_white

    ans = min(ans, sum(diff_black), sum(diff_white))

for i in range(0, y-7):
    for j in range(0, x-7):
        check_diff(i, i+8, j, j+8)

print(ans)
