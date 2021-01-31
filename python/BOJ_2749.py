# n = int(input())
# dp = [0 for _ in range(n+1)]
# dp[1] = 1
#
# for i in range(2, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % 1000000
# print(dp[i] % 1000000)


DIV = 1000000

def solve(n):
    n1, n2 = 0, 1
    for _ in range(n):
        n1, n2 = n2 % DIV, (n1 + n2) % DIV
    return n1

n = int(input())
print(solve(n%(15*(10**5))))
