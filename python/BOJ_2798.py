# n, m = map(int, input().split())
# l = list(map(int, input().split()))
# ans = 0
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             if l[i] + l[j] + l[k] <= m:
#                 ans = max(ans, l[i] + l[j] + l[k])
# print(ans)

n, m = map(int, input().split())
l = sorted(map(int, input().split()), reverse=True)

s = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            t = l[i] + l[j] + l[k]
            if t <= m:
                s.add(t)
                break
print(max(s))
