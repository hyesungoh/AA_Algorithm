import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [10001 for _ in range(k+1)]
dp[0] = 0

for i in range(n):
    t = int(input())
    for j in range(t, k+1):
        dp[j] = min(dp[j], dp[j-t]+1)

print(dp[k] if dp[k] != 10001 else -1)
