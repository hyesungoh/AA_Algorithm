dp = [0 for _ in range(36)]
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, 36):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[int(input())])
