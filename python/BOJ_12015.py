n = int(input())
l = list(map(int, input().split()))
dp = [1 for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(0, i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    ans = max(dp[i], ans)

print(ans)
