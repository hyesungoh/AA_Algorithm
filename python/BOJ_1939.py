import heapq
import sys
input = sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node

    p = find(parent[node])
    parent[node] = p
    return p

def union(a, b):
    pa, pb = find(a), find(b)

    if pa != pb:
        parent[pb] = pa

def solve(s, e):
    while bridges:
        w, n1, n2 = heapq.heappop(bridges)
        w = abs(w)
        union(n1, n2)

        if find(s) == find(e):
            return w


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
bridges = []

for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(bridges, [-w, s, e])

s, e = map(int, input().split())
print(solve(s, e))
