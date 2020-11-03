s1 = input(); l1 = len(s1)
s2 = input(); l2 = len(s2)
dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

for y in range(1, l1+1):
    for x in range(1, l2+1):
        # dp[y][x] = dp[y-1][x-1] + 1 if s1[y-1] == s2[x-1] else max(dp[y-1][x], dp[y][x-1])
        if s1[y-1] == s2[x-1]:
            dp[y][x] = dp[y-1][x-1] + 1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
print(dp[-1][-1])
