import sys
import math
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def query(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end-start+1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        tree[node] += (end-start+1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start + end) // 2
    update_range(node*2, start, mid, left, right, diff)
    update_range(node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

n, m, k = map(int, input().split())

l = []
for _ in range(n): l.append(int(input()))

heigth = math.ceil(math.log2(n))
size = 2 ** (heigth + 1)
tree = [0 for _ in range(size)]
lazy = [0 for _ in range(size)]
init(1, 0, n-1)

for _ in range(m+k):
    t = list(map(int, input().split()))
    if t[0] == 1:
        update_range(1, 0, n-1, t[1]-1, t[2]-1, t[3])
    else:
        print(query(1, 0, n-1, t[1]-1, t[2]-1))
