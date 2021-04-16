
import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra():
    dist = [INF for _ in range(N+1)]
    dist[S] = 0

    q = []
    heapq.heappush(q, [0, S])

    while q:
        w, n = heapq.heappop(q)

        if dist[n] < w:
            continue

        for nn, nw in graph[n]:
            tnw = nw + w
            if dist[nn] > tnw:
                dist[nn] = tnw
                heapq.heappush(q, [tnw, nn])

    return dist


N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

S, E = map(int, input().split())
dist = dijkstra()
print(dist[E])