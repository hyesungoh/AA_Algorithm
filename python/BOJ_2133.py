# def solve(n):
#     dp = [0 for _ in range(31)]
#     dp[0], dp[2] = 1, 3
#     for i in range(4, n+1, 2):
#         dp[i] = dp[i-2] * 3
#         for j in range(i-4, -1, -2):
#             dp[i] += dp[j] * 2
#
#     return dp[n]
#
# n = int(input())
# print(solve(n))

def solve(n):
    dp = [0 for _ in range(31)]
    dp[0], dp[2] = 1, 3

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(0, i-3, 2):
            dp[i] += dp[j] * 2
    return dp[n]

n = int(input())
print(solve(n))
