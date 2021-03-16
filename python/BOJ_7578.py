import sys
from math import log2, ceil
input = sys.stdin.readline

def update(node, start, end, idx):
    if idx < start or end < idx:
        return 0
    if start == end:
        tree[node] = 1
        return 1

    mid = (start + end) // 2
    update(node*2, start, mid, idx)
    update(node*2+1, mid+1, end, idx)
    tree[node] = tree[node*2] + tree[node*2+1]
    return tree[node]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

n = int(input())
l1 = input().split()
idx, l2 = 0, {}
for num in input().split():
    l2[num] = idx
    idx += 1

height = ceil(log2(n))
size = 2 ** (height + 1)
tree = [0 for _ in range(size)]

answer = 0
for num in l1:
    l2_idx = l2[num]
    answer += query(1, 0, n-1, l2_idx, n-1)
    update(1, 0, n-1, l2_idx)
print(answer)
