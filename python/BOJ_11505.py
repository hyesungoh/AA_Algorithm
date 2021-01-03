import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start+end)//2
    temp = init(node*2, start, mid) * init(node*2+1, mid+1, end)
    tree[node] = temp % 1000000007
    return tree[node]

def section_multi(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]

    mid = (start+end)//2
    temp = section_multi(node*2, start, mid, left, right) * section_multi(node*2+1, mid+1, end, left, right)
    return temp % 1000000007

def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    if start == end:
        tree[node] = diff
        return

    mid = (start+end)//2
    update(node*2, start, mid, index, diff)
    update(node*2+1, mid+1, end, index, diff)
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007

n, m, k = map(int, input().split())
l = []
tree = [0 for _ in range(3000000)]

for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        l[b] = c
        update(1, 0, n-1, b, c)
    else:
        print(section_multi(1, 0, n-1, b-1, c-1))
