n, m = map(int, input().split())
l = list(range(1, n+1))
visit = [False] * n
ans = []

def bt(depth):
    if depth == m:
        print(*ans)
        return

    for i in range(n):
        if visit[i]:
            continue

        ans.append(l[i])
        visit[i] = True
        bt(depth+1)
        visit[i] = False
        ans.pop()

bt(0)
