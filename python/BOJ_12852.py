# import heapq
# import sys
# INF = sys.maxsize
#
# def solve():
#     q = []
#     # cnt, visit, now
#     heapq.heappush(q, [0, [n], n])
#     visit = [INF for _ in range(n+1)]
#
#     while q:
#         cnt, route, now = heapq.heappop(q)
#         if now == 1:
#             return cnt, route
#
#         visit[now] = cnt
#
#         heapq.heappush(q, [cnt+1, route+[now-1], now-1])
#
#         div3 = now // 3
#         if now % 3 == 0:
#             heapq.heappush(q, [cnt+1, route+[div3], div3])
#
#         div2 = now // 2
#
#         if now % 2 == 0:
#             heapq.heappush(q, [cnt+1, route+[div2], div2])
#
#
# n = int(input())
# cnt, route = solve()
# print(cnt)
# print(*route)



n = int(input())
dp = [0 for _ in range(n+1)]
paths = [[] for _ in range(n+1)]

dp[1] = 0
paths[1] = [1]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    paths[i] = paths[i-1] + [i]

    div3 = i // 3
    if i % 3 == 0 and dp[i] > dp[div3] + 1:
        dp[i] = dp[div3] + 1
        paths[i] = paths[div3] + [i]

    div2 = i // 2
    if i % 2 == 0 and dp[i] > dp[div2] + 1:
        dp[i] = dp[div2] + 1
        paths[i] = paths[div2] + [i]

print(dp[n])
print(*reversed(paths[n]))
