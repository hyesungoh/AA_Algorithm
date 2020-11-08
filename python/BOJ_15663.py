def bt(depth):
    if depth == m:
        print(*ans)
        return

    temp = 0
    for i in range(n):
        if not visit[i] and temp != l[i]:
            visit[i] = True
            ans.append(l[i])
            temp = l[i]
            bt(depth+1)
            visit[i] = False
            ans.pop()


n, m = map(int, input().split())
l = sorted(map(int, input().split()))
visit = [False for _ in range(n)]
ans = []
bt(0)
