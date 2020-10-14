n, m = map(int, input().split())
l = sorted(map(int, input().split()))
ans = []
visit = {}
for i in l:
    visit[i] = False

def bt(depth):
    if depth == m:
        print(*ans)
        return

    for i in l:
        if visit[i]:
            continue

        ans.append(i)
        visit[i] = True
        bt(depth+1)
        visit[i] = False
        ans.pop()

bt(0)
