# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# visit = [0 for _ in range(n + 1)]
# count = 0
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1
#
# def dfs(node):
#     visit[node] = 1
#     for k in range(1, n+1):
#         if graph[node][k] == 1 and visit[k] == 0:
#             dfs(k)
#
# for i in range(1, n+1):
#     if visit[i] == 0:
#         dfs(i)
#         count += 1
#
# print(count)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(node):
    visit[node] = 1
    for k in range(1, n+1):
        if graph[node][k] and not visit[k]:
            dfs(k)

for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        count += 1

print(count)
