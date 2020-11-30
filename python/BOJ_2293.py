import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
dp[0] = 1

l = []
for _ in range(n):
    l.append(int(input()))

for coin in l:
    for cost in range(1, k+1):
        if cost-coin >= 0:
            dp[cost] += dp[cost-coin]
print(dp[k])
