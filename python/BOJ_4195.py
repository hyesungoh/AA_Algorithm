# import sys
# input = sys.stdin.readline
#
# def countFollow(node):
#     q = [node]
#     followers = [node]
#
#     while q:
#         now = q.pop()
#         if now in graph:
#             for next in graph[now]:
#                 if not next in followers:
#                     followers.append(next)
#                     q.append(next)
#     return len(followers)
#
# for _ in range(int(input())):
#     n = int(input())
#     graph = {}
#     for _ in range(n):
#         a, b = input().split()
#         if a in graph: graph[a].append(b)
#         else: graph[a] = [b]
#         if b in graph: graph[b].append(a)
#         else: graph[b] = [a]
#
#         print(countFollow(a))


import sys
input = sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node

    p = find(parent[node])
    parent[node] = p
    return p

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a != parent_b:
        parent[parent_b] = parent_a
        followers[parent_a] += followers[parent_b]

for _ in range(int(input())):
    n = int(input())
    parent = {}
    followers = {}

    for _ in range(n):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            followers[a] = 1
        if b not in parent:
            parent[b] = b
            followers[b] = 1

        union(a, b)
        print(followers[find(a)])
