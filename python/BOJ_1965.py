# n = int(input())
# l = list(map(int, input().split()))
# dp = [1 for _ in range(n)]
#
# for i in range(n-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if l[i] > l[j]:
#             dp[j] = max(dp[i]+1, dp[j])
#
# print(max(dp))

n = int(input())
l = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
