# def dfs(start):
#     q = [start]
#
#     while q:
#         node = q.pop()
#         is_alive[node] = False
#         for next in graph[node]:
#             q.append(next)
#
# def lif(root):
#     global ans
#     q = [root]
#     while q:
#         node = q.pop()
#         if graph[node] == [] and is_alive[node]:
#             ans += 1
#         elif len(graph[node]) and not is_alive[node]:
#
#         else:
#             for next in graph[node]:
#                 q.append(next)
#
# n = int(input())
# l = list(map(int, input().split()))
# del_node = int(input())
#
# is_alive = [True for _ in range(n)]
# ans = 0
#
# graph = {}
# root = 0
# for i in range(n):
#     graph[i] = []
#     if l[i] != -1:
#         graph[l[i]].append(i)
#     else:
#         root = i
# dfs(del_node)
# lif(root)
#
# print(graph)
# print(is_alive)
# print(ans)


def count_lif(root, del_node):
    global ans
    q = []
    if del_node != root:
        q = [root]

    while q:
        node = q.pop()

        if graph[node] == []:
            ans += 1

        for next in graph[node]:
            if next == del_node:
                if len(graph[node]) == 1:
                    ans += 1
            else:
                q.append(next)

n = int(input())
l = list(map(int, input().split()))
del_node = int(input())

ans = 0
graph = {}
root = 0

for i in range(n):
    graph[i] = []

for i in range(n):
    if l[i] != -1:
        graph[l[i]].append(i)
    else:
        root = i

count_lif(root, del_node)
print(ans)
