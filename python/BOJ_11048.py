# import sys
# from collections import deque
# input = sys.stdin.readline
#
# dire = [[1, 0],
#         [0, 1]]
#
# def bfs():
#     q = deque()
#     q.append([0, 0, graph[0][0]])
#
#     while q:
#         y, x, cnt = q.popleft()
#
#         for dy, dx in dire:
#             ny = dy + y
#             nx = dx + x
#             if 0 <= ny < Y and 0 <= nx < X:
#                 nv = cnt + graph[ny][nx]
#                 if ans[ny][nx] < nv:
#                     ans[ny][nx] = nv
#                     q.append([ny, nx, nv])
#
#
# Y, X = map(int, input().split())
# ans = [[0 for _ in range(X)] for _ in range(Y)]
#
# graph = []
# for _ in range(Y):
#     graph.append(list(map(int, input().split())))
#
# bfs()
# print(ans[Y-1][X-1])

import sys
input = sys.stdin.readline
y, x = map(int, input().split())
graph = []
[graph.append(list(map(int, input().split()))) for _ in range(y)]
dp = [[0 for _ in range(x+1)] for _ in range(y+1)]

for i in range(1, y+1):
    for j in range(1, x+1):
        dp[i][j] = graph[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[y][x])
