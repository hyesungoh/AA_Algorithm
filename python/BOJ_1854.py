import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def solve(n, k, graph):

    q = []
    heapq.heappush(q, [0, 1])
    # k개의 INF로 이루어진 배열이 n+1개
    dists = [[INF for _ in range(k)] for _ in range(n+1)]
    dists[1][0] = 0

    while q:
        cnt, now = heapq.heappop(q)
        for np, tc in graph[now]:
            nc = tc + cnt

            # k번째 수와 비교
            if dists[np][k-1] > nc:
                heapq.heappush(q, [nc, np])
                # k번째 수에 삽입 및 정렬
                dists[np][k-1] = nc
                dists[np].sort()

    return dists

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

dists = solve(n, k, graph)

for i in range(1, n+1):
    print(-1 if dists[i][k-1] == INF else dists[i][k-1])
