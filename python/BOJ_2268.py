import sys
from math import log2, ceil
input = sys.stdin.readline

def query(node, start, end, left, right):
    if start > right or left > end:
        return 0
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, to):
    if index < start or end < index:
        return
    if start == end:
        tree[node] = to
        return
    mid = (start + end) // 2
    update(node*2, start, mid, index, to)
    update(node*2+1, mid+1, end, index, to)
    tree[node] = tree[node*2] + tree[node*2+1]


n, m = map(int, input().split())
height = ceil(log2(n))
size = 2 ** (height + 1)
tree = [0 for _ in range(size)]

for _ in range(m):
    f, i, j = map(int, input().split())
    if f:
        update(1, 0, n - 1, i - 1, j)
    else:
        i, j = (i, j) if i < j else (j, i)
        print(query(1, 0, n - 1, i - 1, j - 1))
