for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for i in range(n):
        for j in range(1, m + 1):
            if j - coins[i] >= 0:
                dp[j] += dp[j-coins[i]]
    print(dp[-1])
