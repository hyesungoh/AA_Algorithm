import sys
input = sys.stdin.readline

n, t = map(int, input().split())
times = []
scores = []
ans = [[0 for _ in range(t+1)] for _ in range(n)]

for _ in range(n):
    tt, ss = map(int, input().split())
    times.append(tt)
    scores.append(ss)

for i in range(n):
    for j in range(t+1):
        time = times[i]
        score = scores[i]
        if j < time:
            ans[i][j] = ans[i-1][j]
        else:
            ans[i][j] = max(ans[i-1][j], score + ans[i-1][j-time])

print(ans[n-1][t])
