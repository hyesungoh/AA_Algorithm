n = int(input())
dp = [0, 1, 1, 2, 2, 1, 2, 1]
for i in range(8, n+1):
    m = min(dp[i-7], dp[i-5], dp[i-2], dp[i-1]) + 1
    dp.append(m)

print(dp[n])
