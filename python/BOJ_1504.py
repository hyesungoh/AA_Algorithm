# import heapq
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize
#
# def dijkstra(start):
#     dist = [INF for _ in range(n+1)]
#     dist[start] = 0
#     q = []
#     heapq.heappush(q, [0, start])
#     while q:
#         weight, here = heapq.heappop(q)
#
#         for there, w in graph[here]:
#             next_weight = weight + w
#             if dist[there] > next_weight:
#                 dist[there] = next_weight
#                 heapq.heappush(q, [next_weight, there])
#     return dist
#
#
# n, e = map(int, input().split())
# graph = {}
#
# for _ in range(e):
#     u, v, w = map(int, input().split())
#     if u not in graph:
#         graph[u] = [[v, w]]
#     else:
#         graph[u].append([v, w])
#     if v not in graph:
#         graph[v] = [[u, w]]
#     else:
#         graph[v].append([u, w])
#
# v1, v2 = map(int, input().split())
# s = dijkstra(1)
# s_v1 = dijkstra(v1)
# s_v2 = dijkstra(v2)
#
# ans = min(s[v1] + s_v1[v2] + s_v2[n],
#           s[v2] + s_v2[v1] + s_v1[n])
# print(ans if ans < INF else -1)

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        weight, here = heapq.heappop(q)

        for there, w in graph[here]:
            next_weight = weight + w
            if dist[there] > next_weight:
                dist[there] = next_weight
                heapq.heappush(q, [next_weight, there])
    return dist


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

v1, v2 = map(int, input().split())
s = dijkstra(1)
s_v1 = dijkstra(v1)
s_v2 = dijkstra(v2)

 # s > v1 > v2 > n과 s > v2 > v1 > n 을 비교
ans = min(s[v1] + s_v1[v2] + s_v2[n],
          s[v2] + s_v2[v1] + s_v1[n])
print(ans if ans < INF else -1)
