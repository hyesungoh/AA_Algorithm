import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
all_cost = sum(costs) + 1
ans = [[0 for _ in range(all_cost)] for _ in range(n)]
result = all_cost

for i in range(n):
    memory = memories[i]
    cost = costs[i]
    for j in range(all_cost):
        if j < cost:
            ans[i][j] = ans[i-1][j]
        else:
            ans[i][j] = max(ans[i-1][j], memory + ans[i-1][j-cost])

        if ans[i][j] >= m:
            result = min(result, j)

print(result)
