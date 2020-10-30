import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bt(depth, ans):
    if depth == m:
        print(*ans[1:])
        return

    for i in l:
        if ans[-1] <= i:
            ans.append(i)
            bt(depth+1, ans)
            ans.pop()

n, m = map(int, input().split())
l = sorted(map(int, input().split()))
bt(0, [0])
