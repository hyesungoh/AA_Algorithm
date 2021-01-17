# n = int(input())
# MAX = n + 1
# dp = [0 for _ in range(MAX)]
# dp[1], dp[2] = 1, 2
#
# for i in range(3, MAX):
#     dp[i] = (dp[i-1] + dp[i-2]) % 10
#
# print(dp[n])


i, j = 1, 1
for _ in range(int(input())):
    i, j = j, (i + j) % 10
print(i)
