n = int(input())
l = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
m = 0
for i in range(n):
    for j in range(0, i):
        if l[i] < l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    m = max(dp[i], m)
print(m+1)
