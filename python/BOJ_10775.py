# import sys
# input = sys.stdin.readline
#
# G = int(input())
# P = int(input())
#
# gates = [False for _ in range(G+1)]
# for i in range(P):
#     t = int(input())
#     for j in range(t, 0, -1):
#         if not gates[j]:
#             gates[j] = True
#             break
#         elif j == 1:
#             print(i)
#             exit()
# print(P)


import sys
input = sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node
    p = find(parent[node])
    parent[node] = p
    return p

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
for i in range(P):
    t = int(input())
    pt = find(t)
    if pt == 0:
        print(i)
        exit()

    union(pt, pt-1)
print(P)
