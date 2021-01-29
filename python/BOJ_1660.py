n = int(input())

coins = []
coin, temp, len_coin = 1, 2, 0
total = 1

while True:
    if total > n:
        break
    coins.append(total)
    coin += temp
    temp += 1
    total += coin

size = len(coins)
dp = [300001 for _ in range(n+1)]
for i in coins:
    dp[i] = 1
dp[0] = 0

for i in range(size):
    for j in range(coins[i], n+1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)

print(dp[n])
