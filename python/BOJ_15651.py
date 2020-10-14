n, m = map(int, input().split())
l = list(range(1, n+1))
ans = []

def bt(depth):
    if depth == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(l[i])
        bt(depth+1)
        ans.pop()
bt(0)
