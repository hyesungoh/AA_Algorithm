# import sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def floyd(graph):
#     for k in range(1, V+1):
#         graph[k][k] = 0
#         for i in range(1, V+1):
#             for j in range(1, V+1):
#                 graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
#
#
# V, E, P = map(int, input().split())
# graph = [[INF for _ in range(V+1)] for _ in range(V+1)]
#
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     graph[s][e] = min(graph[s][e], w)
#     graph[e][s] = min(graph[e][s], w)
#
# floyd(graph)
# print("SAVE HIME" if graph[1][V] == graph[1][P] + graph[P][V] else "GOOD BYE")


import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(start):
    dist = [INF for _ in range(V+1)]
    dist[start] = 0

    q = []
    heapq.heappush(q, [0, start])

    while q:
        w, n = heapq.heappop(q)

        if dist[n] < w:
            continue

        for nn, tw in graph[n]:
            nw = w + tw
            if dist[nn] > nw:
                dist[nn] = nw
                heapq.heappush(q, [nw, nn])

    return dist

V, E, P = map(int, input().split())
graph = {i: [] for i in range(V+1)}
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])


dist = dijkstra(1)
dist_p = dijkstra(P)
print("SAVE HIM" if dist[V] == dist[P] + dist_p[V] else "GOOD BYE")
