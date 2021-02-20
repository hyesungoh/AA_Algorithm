# def solution(n):
#     dp = [0, 1, 2]
#     for i in range(n-2):
#         dp.append(sum(dp[-2:]) % 1000000007)
#
#     return dp[n]

def solution(n):
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b
