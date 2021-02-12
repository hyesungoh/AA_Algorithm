# import sys
# from collections import deque
# input = sys.stdin.readline
#
# dire = [[0,1],[0,-1],[1,0],[-1,0]]
#
# def check(Y, X, r):
#     for y in range(Y-r, Y+r):
#         for x in range(X-r, X+r):
#             if 0 <= y <= max_pos and 0 <= x <= max_pos:
#                 graph[y][x] = 1
#
# def dfs(Y, X, cnt):
#     q = deque()
#     q.append([Y, X])
#     graph[Y][X] = cnt
#
#     while q:
#         y, x = q.popleft()
#         for ty, tx in dire:
#             ny, nx = ty + y, tx + x
#             if 0 <= ny <= max_pos and 0 <= nx <= max_pos:
#                 if graph[ny][nx] == 1:
#                     graph[ny][nx] = cnt
#                     q.append([ny, nx])
#
# for _ in range(int(input())):
#     N = int(input())
#     check_list = []
#     max_pos = 0
#
#     for _ in range(N):
#         y, x, r = map(int, input().split())
#         check_list.append([y, x, r])
#         max_pos = max(max_pos, y, x)
#
#     graph = [[-1 for _ in range(max_pos+1)] for _ in range(max_pos+1)]
#     # visit = [[0 for _ in range(max_pos+1)] for _ in range(max_pos+1)]
#     for y, x, r in check_list:
#         check(y, x, r)
#
#     cnt = 1
#     for y in range(max_pos):
#         for x in range(max_pos):
#             if graph[y][x] == 1:
#                 cnt += 1
#                 dfs(y, x, cnt)
#
#     print(cnt-1)


import sys
input = sys.stdin.readline

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a != parent_b:
        parent[parent_b] = parent_a

def find(node):
    if parent[node] == node:
        return node

    p = find(parent[node])
    parent[node] = p
    return p

for _ in range(int(input())):
    n = int(input())

    parent = [i for i in range(n)]
    ypos = [0 for i in range(n)]
    xpos = [0 for i in range(n)]
    radius = [0 for i in range(n)]

    for i in range(n):
        y, x, r = map(int, input().split())
        ypos[i] = y
        xpos[i] = x
        radius[i] = r

    ans = n
    for i in range(n):
        for j in range(i+1, n):
            ydif = ypos[i] - ypos[j]
            xdif = xpos[i] - xpos[j]
            r = radius[i] + radius[j]

            if (ydif*ydif + xdif*xdif) <= (r*r):
                if find(i) != find(j):
                    union(i, j)
                    ans -= 1

    print(ans)
