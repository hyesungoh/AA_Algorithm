import sys
from math import log2, ceil

INF = sys.maxsize
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return INF

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

def update(node, start, end, index, to):
    if index < start or end < index:
        return tree[node]

    if start == end:
        tree[node] = to
        return tree[node]

    mid = (start + end) // 2
    tree[node] = min(update(node*2, start, mid, index, to), update(node*2+1, mid+1, end, index, to))
    return tree[node]

n = int(input())
l = list(map(int, input().split()))
m = int(input())

height = ceil(log2(n))
size = 2 ** (height + 1)
tree = [INF for _ in range(size)]
init(1, 0, n-1)

for _ in range(m):
    q, i, j = map(int, input().split())
    if q == 1:
        update(1, 0, n-1, i-1, j)
    else:
        print(query(1, 0, n-1, i-1, j-1))
