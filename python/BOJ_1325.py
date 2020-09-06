# import sys
# input = sys.stdin.readline
# from collections import deque
#
# def dfs(graph, start):
#     que = deque()
#     que.append(start)
#     visit = []
#
#     while que:
#         node = que.popleft()
#         if node not in visit:
#             visit.append(node)
#             if node in graph:
#                 que.extend(graph[node])
#     return len(visit)
#
# graph = {}
# n, m = map(int, input().split())
# for _ in range(m):
#     x, y = map(int, input().split())
#     if y in graph:
#         graph[y].append(x)
#     else:
#         graph[y] = [x]
#
# len_list = []
# temp_max = 0
# for i in range(n):
#     temp = dfs(graph, i+1)
#     if temp_max < temp:
#         len_list = [i+1]
#         temp_max = temp
#     elif temp_max == temp:
#         len_list.append(i+1)
#
# print(*len_list)

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in graph[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

len_list = []
temp_max = 0
for i in range(1, n+1):
    temp = bfs(i)
    if temp_max == temp:
        len_list.append(i)
    if temp_max < temp:
        len_list = []
        len_list.append(i)
        temp_max = temp
print(*len_list)
