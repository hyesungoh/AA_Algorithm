n = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
ans = 0
for coin in coins:
    t = n // coin
    n -= t * coin
    ans += t
print(ans)
