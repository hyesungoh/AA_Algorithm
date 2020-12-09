# 11055
# n = int(input())
# l = list(map(int, input().split()))
# dp = l + [0]
# temp = 1001
#
# for i in range(n-1, -1, -1):
#     if l[i] < temp:
#         temp = l[i]
#         dp[i] = dp[i+1] + l[i]
#
#     if dp[i+1] <= l[i]:
#         temp = l[i]
#         dp[i] = l[i]
#
#     dp[i] = max(dp[i], dp[i+1])
# print(dp[0])

n = int(input())
l = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
m = 0

for i in range(n):
    dp[i] = l[i]
    for j in range(0, i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + l[i])
    m = max(m, dp[i])
print(m)
