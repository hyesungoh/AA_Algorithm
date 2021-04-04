
import sys
from math import log2, ceil
input = sys.stdin.readline

MAX = 1000000

def update(node, start, end, index, diff):
    if start > index or index > end:
        return

    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

def query(node, start, end, seq):
    if start == end: return start

    mid = (start + end) // 2
    # 왼쪽으로 탐색
    if tree[node * 2] >= seq:
        return query(node * 2, start, mid, seq)
    # 오른쪽으로 탐색
    else:
        return query(node * 2 + 1, mid + 1, end, seq - tree[node * 2])


height = ceil(log2(MAX))
size = 2 ** (height + 1)
tree = [0 for _ in range(size)]


for _ in range(int(input())):
    ip = list(map(int, input().split()))
    if ip[0] == 1:
        index = query(1, 0, MAX-1, ip[1])
        print(index)
        update(1, 0, MAX-1, index, -1)

    else:
        update(1, 0, MAX-1, ip[1], ip[2])