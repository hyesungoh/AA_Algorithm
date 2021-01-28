import sys
INF = sys.maxsize
input = sys.stdin.readline

def solve():
    dist = graph
    route = [[i for i in range(n+1)] for _ in range(n+1)]

    for k in range(1, n+1):
        dist[k][k] = 0
        route[k][k] = "-"

        for i in range(1, n+1):
            for j in range(1, n+1):
                next = graph[i][k] + graph[k][j]
                if dist[i][j] > next:
                    dist[i][j] = next
                    route[i][j] = route[i][k]

    return route

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)
    graph[e][s] = min(graph[e][s], w)

for r in solve()[1:]:
    print(" ".join(map(lambda x: str(x), r[1:])))


# import sys
# INF = sys.maxsize
# r = sys.stdin.readline
#
# n, m = map(int, r().split())
# g = [[INF] * (n+1) for _ in range(n+1)]
# ro = [[i for i in range(n+1)] for _ in range(n+1)]
#
# for _ in range(m):
#     s, e, w = map(int, r().split())
#     g[s][e] = min(g[s][e], w)
#     g[e][s] = min(g[e][s], w)
#
#
# for k in range(1, n+1):
#     g[k][k] = 0
#     ro[k][k] = "-"
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             ne = g[i][k] + g[k][j]
#             if g[i][j] > ne:
#                 g[i][j] = ne
#                 ro[i][j] = ro[i][k]
#
# for s in ro[1:]:
#     print(" ".join(map(lambda x: str(x), s[1:])))
