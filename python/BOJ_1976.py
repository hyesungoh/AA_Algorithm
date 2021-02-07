# import sys
# input = sys.stdin.readline
#
# def solve():
#     for i in range(m - 1):
#         now = dist[i]
#         next = dist[i + 1]
#         if not graph[now][next]:
#             return False
#     return True
#
# n = int(input())
# m = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
#
# for k in range(n):
#     graph[k][k] = 1
#     for i in range(n):
#         for j in range(n):
#                 if graph[i][k] and graph[k][j]:
#                     graph[i][j] = 1
#
# dist = list(map(lambda x: int(x)-1, input().split()))
#
# print("YES" if solve() else "NO")


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


n = int(input())
m = int(input())
parent = [i for i in range(n)]

for i in range(n):
    linked = list(map(int, input().split()))
    for j in range(n):
        if linked[j]:
            union(i, j)

plan = list(map(int, input().split()))
ans = set([find(parent[i-1])for i in plan])
print("YES" if len(ans) == 1 else "NO")
