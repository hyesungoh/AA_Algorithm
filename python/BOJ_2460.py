t, ans = 0, 0
for _ in range(10):
    i, j = map(int, input().split())
    t = t + j - i
    ans = max(ans, t)

print(ans)
