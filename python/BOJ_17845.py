import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(K)]
impos = []
times = []
for _ in range(K):
    i, t = map(int, input().split())
    impos.append(i)
    times.append(t)

for k in range(K):

    now_impo = impos[k]
    now_time = times[k]
    for time in range(N+1):
        if time < now_time:
            dp[k][time] = dp[k-1][time]
        else:
            dp[k][time] = max(dp[k-1][time], dp[k-1][time-now_time] + now_impo)


print(dp[-1][N])
