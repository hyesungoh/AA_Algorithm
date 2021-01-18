def solve(n):
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))
    ans = [[0 for _ in range(100)] for _ in range(n)]

    if n == 0:
        return 0
    if n == 1:
        return value[0] if weight[0] <= 99 else 0

    for v in range(n):
        for w in range(100):
            val = value[v]
            cost = weight[v]
            if w < cost:
                ans[v][w] = ans[v - 1][w]
            else:
                ans[v][w] = max(ans[v - 1][w], val + ans[v - 1][w - cost])

    return ans[n - 1][99]

n = int(input())
print(solve(n))
