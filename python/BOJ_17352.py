import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find(node):
    if node == parents[node]:
        return node
    p = find(parents[node])
    parents[node] = p
    return p

def union(a, b):
    pa, pb = find(a), find(b)

    if pa != pb:
        parents[pb] = pa

n = int(input())
parents = [i for i in range(n+1)]

for _ in range(n-2):
    s, e = map(int, input().split())
    union(s, e)

first = find(1)
for i in range(2, n+1):
    if find(i) != first:
        print(1, i)
        sys.exit(0)
