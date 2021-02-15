import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    dist = [INF for _ in range(n+1)]
    dist[x] = 0

    q = []
    heapq.heappush(q, [0, x])
    while q:
        cnt, now = heapq.heappop(q)
        for nn, nd in graph[now]:
            nextd = nd + cnt
            if dist[nn] > nextd:
                heapq.heappush(q, [nextd, nn])
                dist[nn] = nextd
    return dist

n, m, k, x = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append([e, 1])

dist = dijkstra()
ans = list(filter(lambda i: dist[i] == k, range(1, n+1)))
[print(i) for i in ans] if len(ans) else print(-1)
