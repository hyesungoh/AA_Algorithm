import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start, dist, graph):
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        cnt, here = heapq.heappop(q)
        if dist[here] > cnt:
            dist[here] = cnt

        for there in range(1, n+1):
            if dist[there] > cnt + graph[here][there]:
                heapq.heappush(q, [cnt + graph[here][there], there])


n, m, x = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
graph_r = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)
    graph_r[e][s] = min(graph_r[e][s], w)

dist_x = [INF for _ in range(n+1)]
dist_r = [INF for _ in range(n+1)]
dijkstra(x, dist_x, graph)
dijkstra(x, dist_r, graph_r)

ans = 0
for i in range(1, n+1):
    ans = max(ans, dist_x[i] + dist_r[i])
print(ans)
