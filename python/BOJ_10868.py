import sys
INF = sys.maxsize
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return INF
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

n, m = map(int, input().split())
l = []
tree = [INF for _ in range(333333)]
for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

for _ in range(m):
    s, e = map(int, input().split())
    print(query(1, 0, n-1, s-1, e-1))
