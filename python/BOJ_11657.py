# import sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def relax():
#     for start in range(n+1):
#         for end, weight in graph[start]:
#             next_weight = dist[start] + weight
#             if dist[end] > next_weight:
#                 dist[end] = next_weight
#     return dist
#
# def bellman():
#     for start in range(n+1):
#         for end, weight in graph[start]:
#             next_weight = dist[start] + weight
#             if dist[end] > next_weight:
#                 return False
#     return True
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# dist = [INF for _ in range(n+1)]
# dist[1] = 0
#
# for _ in range(m):
#     s, e, w = map(int, input().split())
#     graph[s].append([e, w])
#
# short = relax()
#
# if bellman():
#     for i in range(2, n+1):
#         print(short[i] if short[i] != INF else -1)
# else:
#     print(-1)

import sys
INF = sys.maxsize
input = sys.stdin.readline

def bellman():
    for i in range(1, n+1):
        for start in range(1, n+1):
            for end, weight in graph[start]:
                next_weight = weight + dist[start]
                if dist[end] > next_weight:
                    if i == n and next_weight < 60000001:
                        print(-1)
                        sys.exit(0)
                    dist[end] = next_weight

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
dist[1] = 0

for _ in range(m):
    s, e, w = map(int, input().rstrip().split())
    graph[s].append([e, w])

bellman()

for i in dist[2:]:
    print(i if i < 60000001 else -1)