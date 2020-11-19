import sys
input = sys.stdin.readline

n = int(input())
dp = [0]
l = [0]
for _ in range(n):
    t = int(input())
    dp.append(t)
    l.append(t)

if n == 1:
    print(dp[1])
    exit(0)

dp[2] = dp[1] + dp[2]
for i in range(3, n+1):
    dp[i] = max(l[i] + l[i-1] + dp[i-3], l[i] + dp[i-2], dp[i-1])

print(dp[-1])
