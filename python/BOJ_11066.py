import sys
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    N = int(input())
    sizes = list(map(int, input().split()))

    dp = [[0 for _ in range(N)] for _ in range(N)]
    acc_sum = [0]
    for size in sizes: acc_sum.append(acc_sum[-1] + size)

    for d in range(1, N):
        for i in range(N-d):
            j = d + i
            dp[i][j] = INF
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + acc_sum[j+1] - acc_sum[i])

    print(dp[0][N-1])
