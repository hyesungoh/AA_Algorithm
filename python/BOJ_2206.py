# 재귀 형식으로 구현 > 메모리 초과 결과
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
#
# def find(y, x, isBreak):
#     if y == Y-1 and x == X-1:
#         return
#
#     for h, w in direc:
#         ty = y + h
#         tx = x + w
#
#         if 0 <= ty < Y and 0 <= tx < X:
#             if graph[ty][tx] == 0 and dist[ty][tx] > dist[y][x]+1:
#                 dist[ty][tx] = dist[y][x]+1
#                 find(ty, tx, isBreak)
#
#             elif graph[ty][tx] == 1 and isBreak == False and dist[ty][tx] > dist[y][x]+1:
#                 dist[ty][tx] = dist[y][x]+1
#                 isBreak = True
#                 find(ty, tx, isBreak)
#
#
# MS = 1000001
# Y, X = map(int, input().strip().split())
# graph = []
# dist = [[MS for _ in range(X)] for _ in range(Y)]
# dist[0][0] = 1
#
# direc = [[0, 1],
#          [0, -1],
#          [1, 0],
#          [-1, 0]]
#
# for i in range(Y):
#     graph.append(list(map(int, input().strip())))
#
# find(0, 0, False)
#
# print(dist[Y-1][X-1] if dist[Y-1][X-1] != MS else -1)

# deque로 구현

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, 0])

    while q:
        y, x, is_break = q.popleft()

        if y == Y-1 and x == X-1:
            return dist[is_break][y][x]

        for h, w in direc:
            ty = y + h
            tx = x + w

            if 0 <= ty < Y and 0 <= tx < X:
                if graph[ty][tx] == 0 and dist[is_break][ty][tx] == 0:
                    dist[is_break][ty][tx] = dist[is_break][y][x]+1
                    q.append([ty, tx, is_break])

                elif graph[ty][tx] == 1 and is_break == 0:
                    dist[1][ty][tx] = dist[0][y][x]+1
                    q.append([ty, tx, 1])
    return -1


Y, X = map(int, input().split())
graph = []
dist = [[[0 for _ in range(X)] for _ in range(Y)] for _ in range(2)]
dist[0][0][0] = 1

direc = [[0, 1],
         [0, -1],
         [1, 0],
         [-1, 0]]

for i in range(Y):
    graph.append(list(map(int, input().strip())))

print(bfs())
