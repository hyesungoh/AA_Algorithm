n = int(input())
size = 1000001

if n == 0:
    print("0\n0")
    exit(0)
print(-1) if n % 2 == 0 and n < 0 else print(1)

n = abs(n)

dp = [0 for _ in range(size)]
dp[1] = 1
for i in range(2, size): dp[i] = (dp[i-1] + dp[i-2]) % 1000000000
print(dp[n])
