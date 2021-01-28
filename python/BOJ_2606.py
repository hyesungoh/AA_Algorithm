# def dfs(graph):
#     visit = []
#     stack = [1]
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             if node in graph:
#                 stack.extend(graph[node])
#     return visit
#
# graph = {}
# input()
# for _ in range(int(input())):
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
# print(len(dfs(graph))-1)

# def solve():
#     visit = [False for _ in range(n+1)]
#     visit[1] = True
#     q = [1]
#     ans = 0
#
#     while q:
#         node = q.pop()
#         for next_node in graph[node]:
#             if not visit[next_node]:
#                 visit[next_node] = True
#                 q.append(next_node)
#                 ans += 1
#     return ans
#
# n = int(input())
# m = int(input())
# graph = {i: [] for i in range(1, n+1)}
#
# for _ in range(m):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)
# print(solve())

def solve():
    visit = [False for _ in range(n+1)]
    q = [1]

    while q:
        node = q.pop()
        if not visit[node]:
            visit[node] = True
            q.extend(graph[node])

    return visit.count(True) - 1

n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

print(solve())
