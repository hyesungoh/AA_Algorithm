import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(n)]
p = [0 for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    ti, pi = map(int, input().split())
    t[i] = ti
    p[i], dp[i] = pi, pi

for i in range(n-1, -1, -1):
    if n < i + t[i]:
        dp[i] = dp[i+1]
        continue
    dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])

print(dp[0])
