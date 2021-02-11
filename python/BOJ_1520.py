# dire = [[1, 0],
#         [-1, 0],
#         [0, 1],
#         [0, -1]]
#
# Y, X = map(int, input().split())
# graph = [[] for _ in range(Y)]
# for i in range(Y): graph[i] = list(map(int, input().split()))
# dp = [[0 for _ in range(X)] for _ in range(Y)]
# dp[0][0] = 1
#
# for y in range(Y):
#     for x in range(X):
#         for ty, tx in dire:
#             ny = y + ty
#             nx = x + tx
#             if 0 <= ny < Y and 0 <= nx < X:
#                 if graph[ny][nx] < graph[y][x]:
#                     dp[ny][nx] += dp[y][x]
#                     print(y, x)
#
# for i in dp:
#     print(i)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(y, x):
    if Y-1 == y and X-1 == x:
        return 1

    if dp[y][x] == -1:
        dp[y][x] = 0
        for ty, tx in dire:
            ny, nx = y + ty, x + tx
            if 0 <= ny < Y and 0 <= nx < X:
                if graph[y][x] > graph[ny][nx]:
                    dp[y][x] += dfs(ny, nx)
    return dp[y][x]

dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]
Y, X = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
dp = [[-1 for _ in range(X)] for _ in range(Y)]

dfs(0, 0)
print(dp[0][0])
