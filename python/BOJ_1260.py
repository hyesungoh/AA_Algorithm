# from collections import deque
#
# def dfs(gra, sta):
#     vis = []
#     stack = deque([sta])
#     while stack:
#         nod = stack.pop()
#         if nod not in vis:
#             vis.append(nod)
#             if nod in gra:
#                 stack.extend(sorted(gra[nod], reverse=True))
#     return " ".join(str(i) for i in vis)
#
# def bfs(gra, sta):
#     vis = []
#     que = deque([sta])
#     while que:
#         nod = que.popleft()
#         if nod not in vis:
#             vis.append(nod)
#             if nod in gra:
#                 que.extend(sorted(gra[nod]))
#
#     return " ".join(str(i) for i in vis)
#
# graph = {}
# n, m, start = map(int, input().split())
# for _ in range(m):
#     x, y = map(int, input().split())
#     if x in graph:
#         graph[x].append(y)
#     else:
#         graph[x] = [y]
#     if y in graph:
#         graph[y].append(x)
#     else:
#         graph[y] = [x]
#
# print(dfs(graph, start))
# print(bfs(graph, start))

import sys
from collections import deque
input = sys.stdin.readline

def solve(start, is_bfs):
    q = deque() if is_bfs else []
    q.append(start)
    visit = [False for _ in range(n+1)]
    ans = []

    while q:
        now = q.popleft() if is_bfs else q.pop()
        if not visit[now]:
            visit[now] = True
            ans.append(str(now))
            if now in graph:
                q.extend(sorted(graph[now]) if is_bfs else sorted(graph[now], reverse=True))

    return " ".join(ans)

n, m, v = map(int, input().split())
graph = {}
for _ in range(m):
    s, e = map(int, input().split())
    if s in graph: graph[s].append(e)
    else: graph[s] = [e]
    if e in graph: graph[e].append(s)
    else: graph[e] = [s]

print(solve(v, False))
print(solve(v, True))
