n = int(input())
dp = [[1 for _ in range(10)] for _ in range(n)]
dp[0][0] = 0

for y in range(1, n):
    for x in range(10):
        if x == 0:
            dp[y][x] = dp[y-1][1]
        elif x == 9:
            dp[y][x] = dp[y-1][8]
        else:
            dp[y][x] = dp[y-1][x-1] + dp[y-1][x+1]

print(sum(dp[n-1]) % 1000000000)
