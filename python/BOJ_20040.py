import sys
input = sys.stdin.readline

def find(node):
    if node == parents[node]:
        return node
    p = find(parents[node])
    parents[node] = p
    return p

def union(a, b):
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())
parents = [i for i in range(n)]
isCycle = [False for _ in range(n)]


for cnt in range(m):
    a, b = map(find, (map(int, input().split())))
    if a == b:
        print(cnt + 1)
        exit(0)
    union(a, b)
print(0)
