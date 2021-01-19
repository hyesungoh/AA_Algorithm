import sys
input = sys.stdin.readline

def solve(n, m, costs, prices):
    m += 1
    ans = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        cost = costs[i]
        price = prices[i]
        for j in range(m):
            if j < price:
                ans[i][j] = ans[i-1][j]
            else:
                ans[i][j] = max(ans[i-1][j], cost + ans[i][j-price], cost + ans[i - 1][j - price])

    return ans[n-1][m-1]

while True:
    n, m = map(float, input().split())
    if n == 0 and m == 0:
        break
    n = int(n)
    m = round(m * 100)


    costs = []
    prices = []
    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = round(p * 100)
        costs.append(c)
        prices.append(p)

    print(solve(n, m, costs, prices))
