# n = int(input())
# l = [0] + list(map(int, input().split()))
# max = 0
#
# for i in range(1, n+1):
#     cost = ((n // i) * l[i]) + l[n % i]
#     if max < cost:
#         max = cost
# print(max)
#
# 10
# 1 100 160 1 1 1 1 1 1 1
# 위 반례에서 실패

n = int(input())
l = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

dp[1] = l[1]
for i in range(2, n+1):
    for j in range(1, (i//2) + 1):
        dp[i] = max(l[i], dp[i], dp[j] + dp[i-j])
print(dp[n])
