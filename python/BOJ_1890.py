# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def solve():
#     q = deque()
#     q.append([0, 0])
#     dp[0][0] = 1
#
#     while q:
#         y, x = q.popleft()
#         move = graph[y][x]
#         if move == 0:
#             continue
#         ny, nx = y + move, x + move
#
#         if 0 <= ny < n:
#             q.append([ny, x])
#             dp[ny][x] += dp[y][x]
#
#         if 0 <= nx < n:
#             q.append([y, nx])
#             dp[y][nx] += dp[y][x]
#
#
# n = int(input())
# graph = [[] for _ in range(n)]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n): graph[i] = list(map(int, input().split()))
#
# solve()
# print(dp[n-1][n-1])


import sys
input = sys.stdin.readline

def solve():
    dp[0][0] = 1

    for y in range(n):
        for x in range(n):
            if y == n-1 and x == n-1:
                break
            move = graph[y][x]
            ny, nx = y + move, x + move

            if 0 <= ny < n:
                dp[ny][x] += dp[y][x]

            if 0 <= nx < n:
                dp[y][nx] += dp[y][x]


n = int(input())
graph = [[] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n): graph[i] = list(map(int, input().split()))

solve()
print(dp[n-1][n-1])
