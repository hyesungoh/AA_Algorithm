# import sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def floyd():
#     get = [items[i] for i in range(n+1)]
#
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             if graph[i][k] <= m:
#                 get[i] += items[k]
#
#             for j in range(1, n+1):
#                 if graph[i][k] + graph[k][j] <= m:
#                     get[i] += items[j]
#
#     return max(get)
#
# n, m, r = map(int, input().split())
# items = [0] + list(map(int, input().split()))
# graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
#
# for _ in range(r):
#     s, e, w = map(int, input().split())
#     graph[s][e] = min(graph[s][e], w)
#     graph[e][s] = min(graph[e][s], w)
#
# ans = floyd()
# print(ans)

import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    visit = [False for _ in range(n+1)]
    visit[start] = True
    item = items[start]

    while q:
        weight, node = heapq.heappop(q)

        for nn, nw in graph[node]:
            next_weight = weight + nw
            if next_weight <= m:
                heapq.heappush(q, [next_weight, nn])

                if not visit[nn]:
                    visit[nn] = True
                    item += items[nn]

    return item

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = {i: [] for  i in range(1, n+1)}

for _ in range(r):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

ans = 0
for i in range(1, n+1):
    ans = max(ans, dijkstra(i))
print(ans)
