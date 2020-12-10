from collections import deque
import sys
input = sys.stdin.readline

dire = [[2, -1], # 상 좌
        [2, 1], # 상 우
        [1, 2], # 우 상
        [-1, 2], # 우 하
        [-2, 1], # 하 우
        [-2, -1], # 하 좌
        [1, -2], # 좌 상
        [-1, -2]] # 좌 하


# def bfs(start, goal_y, goal_x):
#     q = deque()
#     q.append(start + [0])
#     while q:
#         now_y, now_x, cnt = q.popleft()
#
#         if now_y == goal_y and now_x == goal_x:
#             return cnt
#
#         for dire_y, dire_x in dire:
#             next_y = now_y + dire_y
#             next_x = now_x + dire_x
#             if 0 <= next_y < size and 0 <= next_x < size:
#                 if not board[next_y][next_x]:
#                     q.append([next_y, next_x, cnt+1])
#                     board[next_y][next_x] = True
# t = int(input())
# for _ in range(t):
#     size = int(input())
#     board = [[False for _ in range(size)] for _ in range(size)]
#     start_y, start_x = map(int, input().split())
#     goal_y, goal_x = map(int, input().split())
#
#     ans = bfs([start_y, start_x], goal_y, goal_x)
#     print(ans)


def bfs(start_y, start_x, goal_y, goal_x):
    q = deque()
    q.append([start_y, start_x])
    board[start_y][start_x] = 1

    while q:
        now_y, now_x = q.popleft()

        if now_y == goal_y and now_x == goal_x:
            return board[now_y][now_x] - 1

        for dire_y, dire_x in dire:
            next_y = now_y + dire_y
            next_x = now_x + dire_x
            if 0 <= next_y < size and 0 <= next_x < size:
                if board[next_y][next_x] == 0:
                    q.append([next_y, next_x])
                    board[next_y][next_x] = board[now_y][now_x] + 1

t = int(input())
for _ in range(t):
    size = int(input())
    board = [[0 for _ in range(size)] for _ in range(size)]
    start_y, start_x = map(int, input().split())
    goal_y, goal_x = map(int, input().split())

    if start_y == goal_y and start_x == goal_x:
        print(0)
        continue

    ans = bfs(start_y, start_x, goal_y, goal_x)
    print(ans)
