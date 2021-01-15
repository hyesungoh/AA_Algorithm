import sys
input = sys.stdin.readline

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = sum(dp[i-3:i]) % 1000000009

for i in range(int(input())):
    print(dp[int(input())] % 1000000009)
