# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
#
# def find(node):
#     if node == parents[node]:
#         return node
#
#     p = find(parents[node])
#     parents[node] = p
#     return p
#
# def union(a, b):
#     pa, pb = find(a), find(b)
#
#     if pa != pb:
#         parents[pb] = pa
#     else:
#         parents[pa] = 0
#         parents[pb] = 0
#
# def output(i, n):
#     if n == 0:
#         print("Case %d: No trees." %i)
#     elif n == 1:
#         print("Case %d: There is one tree." %i)
#     else:
#         print("Case %d: A forest of %d trees." %(i, n))
#
# index = 1
# while True:
#     n, m = map(int, input().split())
#     if n == m == 0: break
#
#     parents = [i for i in range(n+1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         union(a, b)
#
#     tree = set(find(i) for i in parents)
#     output(index, len(tree)-1)
#     index += 1


import sys
input = sys.stdin.readline

def find(node):
    if node == -1:
        return 0
    if node == parents[node]:
        return node

    p = find(parents[node])
    parents[node] = p
    return p

def union(a, b):
    if a < b:
        if iscycle[b]: iscycle[a] = True
        parents[b] = a
    else:
        if iscycle[a]: iscycle[b] = True
        parents[a] = b

def output(i, n):
    if n == 0:
        print("Case %d: No trees." %i)
    elif n == 1:
        print("Case %d: There is one tree." %i)
    else:
        print("Case %d: A forest of %d trees." %(i, n))

index = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0: break

    parents = [i for i in range(n+1)]
    iscycle = [False for i in range(n+1)]

    for _ in range(m):
        a, b = map(find, map(int, input().split()))
        if a == b:
            iscycle[a] = True
        else:
            union(a, b)

    ans = 0
    for i in range(1, n+1):
        pi = find(i)
        if not iscycle[pi]:
            ans += 1
            iscycle[pi] = True

    output(index, ans)
    index += 1
