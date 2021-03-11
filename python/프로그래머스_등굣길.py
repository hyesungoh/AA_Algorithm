def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for px, py in puddles:
        dp[py][px] = -1

    for y in range(1, n+1):
        for x in range(1, m+1):
            if y == 1 and x == 1:
                continue
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue

            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000007

    return dp[n][m]
