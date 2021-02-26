def bt(depth):
    if depth == n:
        print(*nl)
        return

    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = True
            nl.append(i)

            bt(depth+1)

            visit[i] = False
            nl.pop()

n = int(input())
nl = []
visit = [False for _ in range(n+1)]
bt(0)
