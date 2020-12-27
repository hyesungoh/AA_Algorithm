def calcur(tl):
    t = 0
    for i in range(n-1):
        t += abs(tl[i] - tl[i+1])
    return t

def bt(depth, tl):
    if depth == n:
        ans.append(calcur(tl))
        return

    for i in range(n):
        if visit[i]:
            continue

        visit[i] = True
        tl.append(l[i])
        bt(depth+1, tl)
        visit[i] = False
        tl.pop()


n = int(input())
l = list(map(int, input().split()))
visit = [False for _ in range(n)]
tl = []
ans = []

bt(0, tl)
print(max(ans))
