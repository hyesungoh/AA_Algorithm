# MAX = 1000 * 100 + 1
#
# c, n = map(int, input().split())
# # dp[비용] = 최대한 구할 수 있는 사람의 수
# dp = [0 for _ in range(MAX)]
#
# cost = [0 for _ in range(n)]
# customer = [0 for _ in range(n)]
# for i in range(n):
#     cost[i], customer[i] = map(int, input().split())
#
# for i in range(n):
#     for j in range(cost[i], MAX):
#         dp[j] = max(dp[j], dp[j-cost[i]] + customer[i])
#
# for i in range(MAX):
#     if dp[i] >= c:
#         print(i)
#         exit(0)


# 최대 1000명, 홍보 최대 비용 100
MAX_COST = 1000 * 100 + 1
MAX_CUSTOMER = 1000 + 100 + 1

c, n = map(int, input().split())
# dp[사람의 수] = 최소한의 비용
# 최대 인원 + 홍보 최대 인원 100명까지 비교하면 됨
dp = [MAX_COST for _ in range(MAX_CUSTOMER)]
dp[0] = 0

for i in range(n):
    cost, customer = map(int, input().split())
    for j in range(customer, MAX_CUSTOMER):
        dp[j] = min(dp[j], dp[j-customer] + cost)

print(min(dp[c:-1]))
