n, m = map(int, input().split())
l = list(range(1, n+1))
ans = []

def bt(depth, index):
    if depth == m:
        print(*ans)
        return

    for i in range(n):
        if l[i] >= index:
            ans.append(l[i])
            bt(depth + 1, l[i])
            ans.pop()

bt(0, 0)
