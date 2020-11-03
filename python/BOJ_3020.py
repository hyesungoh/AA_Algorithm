# 3020
# import sys
# input = sys.stdin.readline
#
# n, h = map(int, input().split())
# dist = [[0 for _ in range(h)] for _ in range(n+1)]
#
# for i in range(1, n+1):
#     t = int(input())
#
#     if i % 2 == 1:
#         for j in range(h):
#             dist[i][j] = dist[i-1][j] + 1 if j < t else dist[i - 1][j]
#     else:
#         for j in range(h):
#             dist[i][j] = dist[i-1][j] + 1 if j >= t-1 else dist[i - 1][j]
#
# m = min(dist[-1])
# print(m, dist[-1].count(m))

import sys
input = sys.stdin.readline

n, h = map(int, input().split())
btm = [0 for _ in range(h+1)]
high = [0 for _ in range(h+1)]
dist = [0 for _ in range(h+1)]

for i in range(n):
    if i % 2 == 0:
        btm[int(input())] += 1
    else:
        high[int(input())] += 1

for i in range(h-1, 0, -1):
    btm[i] = btm[i+1] + btm[i]
    high[i] = high[i+1] + high[i]

for i in range(1, h+1):
    dist[i] = btm[i]+high[h-i+1]

dist = dist[1:]
m = min(dist[1:])
print(m, dist.count(m))
