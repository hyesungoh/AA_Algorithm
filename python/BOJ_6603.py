import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bt(depth):
    if depth == 6:
        print(*ans)
        return

    for i in range(n):
        if not visit[i]:
            ans.append(l[i])
            visit[i] = True
            bt(depth+1)
            ans.pop()
            for j in range(i+1, n):
                visit[j] = False

while True:
    s = list(map(int, input().split()))
    if s == [0]:
        break
    n = s[0]
    l = s[1:n+1]
    visit = [False for _ in range(n)]
    ans = []
    bt(0)
    print("")
