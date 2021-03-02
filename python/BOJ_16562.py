import sys
input = sys.stdin.readline

def find(node):
    if parents[node] == node:
        return node

    p = find(parents[node])
    parents[node] = p
    return p

def union(a, b):
    pa, pb = find(a), find(b)

    if pa != pb:
        if pay[pa] < pay[pb]:
            parents[pb] = pa
        else:
            parents[pa] = pb

n, m, k = map(int, input().split())
pay = [0] + list(map(int, input().split()))
parents = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

set_parents = set()
for i in range(1, n+1):
    set_parents.add(find(i))

ans = sum(map(lambda x: pay[x], set_parents))
print(ans if ans <= k else "Oh no")
