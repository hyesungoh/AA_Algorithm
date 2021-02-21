import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra():
    q = []
    dist = [INF for _ in range(n)]
    heapq.heappush(q, [0, 0])
    dist[0] = 0

    while q:
        w, now = heapq.heappop(q)

        if w > dist[now]:
            continue

        for tw, nn in graph[now]:
            nw = w + tw
            if dist[nn] > nw:
                heapq.heappush(q, [nw, nn])
                dist[nn] = nw
    return dist[-1] if dist[-1] != INF else -1


n, m = map(int, input().split())
sight = list(map(int, input().split()))
sight[n-1] = 0
graph = {i: [] for i in range(n)}

for _ in range(m):
    s, e, w = map(int, input().split())
    if sight[s] == 1 or sight[e] == 1:
        continue
    graph[s].append([w, e])
    graph[e].append([w, s])

print(dijkstra())
