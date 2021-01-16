import sys
import math
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start + end) // 2
    temp = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    tree[node] = temp
    return tree[node]

def query(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    temp = query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)
    return temp

def update(node, start, end, index, diff):
    if index < start or index > end:
        return 0

    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)


n, q = map(int, input().split())
l = list(map(int, input().split()))

# 세그먼트 트리 크기
height = math.ceil(math.log2(n))
size = 2 ** (height + 1)
tree = [0 for _ in range(size)]
init(1, 0, n-1)

for _ in range(q):
    left, right, cindex, cvalue = map(int, input().split())
    if right < left:
        left, right = right, left
    print(query(1, 0, n-1, left-1, right-1))

    diff = cvalue - l[cindex-1]
    l[cindex-1] = cvalue
    update(1, 0, n-1, cindex-1, diff)
