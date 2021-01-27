import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

def solve(start, node_num):
    q = []
    heapq.heappush(q, [0, start])

    dist = [INF for _ in range(node_num+1)]
    dist[start] = 0

    while q:
        s, n = heapq.heappop(q)
        for nn, ts in graph[n]:
            ns = ts + s
            if dist[nn] > ns:
                dist[nn] = ns
                heapq.heappush(q, [ns, nn])

    return dist

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    dist = solve(c, n)
    visited, second = 0, 0
    for temp in dist:
        if temp != INF:
            visited += 1
            second = max(second, temp)
    print(visited, second)
