import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def solve(n, graph, S, E):
    dist = [INF for _ in range(n+1)]
    visited = [[] for _ in range(n+1)]
    q = []

    # cost, current position, visited position
    heapq.heappush(q, [0, S])
    dist[S] = 0
    visited[S] = [S]

    while q:
        cost, now = heapq.heappop(q)

        if cost > dist[now]:
            continue

        for np, tc in graph[now]:
            nc = cost + tc
            if nc < dist[np]:
                heapq.heappush(q, [nc, np])
                dist[np] = nc

                visited[np] = []
                for v in visited[now]:
                    visited[np].append(v)
                visited[np].append(np)

    return dist[E], visited[E]

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

S, E = map(int, input().split())

d, v = solve(n, graph, S, E)
print(d)
print(len(v))
print(*v)
