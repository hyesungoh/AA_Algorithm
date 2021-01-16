dp = [0 for _ in range(51)]
dp[0], dp[1] = 1, 1
for i in range(2, 51):
    dp[i] = (1 + dp[i-1] + dp[i-2]) % 1000000007

print(dp[int(input())] % 1000000007)
