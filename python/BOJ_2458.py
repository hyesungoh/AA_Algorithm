# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# compare = [[False for _ in range(n+1)] for _ in range(n+1)]
# d = [[False for _ in range(n+1)] for _ in range(n+1)]
#
# for _ in range(m):
#     s, e = map(int, input().split())
#     compare[s][e] = True
#     compare[e][s] = True
#     d[s][e] = True
#
# for k in range(1, n+1):
#     compare[k][k] = True
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if d[i][k] and d[k][j]:
#                 compare[i][j] = True
#                 compare[j][i] = True
#
# ans = 0
# for i in range(1, n+1):
#     if compare[i][1:n+1].count(False) == 0:
#         ans += 1
# print(ans)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
compare = [[False for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    compare[s][e] = True

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if compare[i][k] and compare[k][j]:
                compare[i][j] = True

ans = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if compare[i][j]:
            ans[i] += 1
            ans[j] += 1

print(ans.count(n-1))
