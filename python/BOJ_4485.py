import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

dire = [[1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]]


def dijk(n):
    dist = [[INF for _ in range(n)] for _ in range(n)]
    q = []

    dist[0][0] = graph[0][0]
    heapq.heappush(q, [dist[0][0], 0, 0])

    while q:
        now_dist, y, x = heapq.heappop(q)
        for ty, tx in dire:
            ny = y + ty
            nx = x + tx

            if 0 <= ny < n and 0 <= nx < n:
                ndist = now_dist + graph[ny][nx]
                if dist[ny][nx] > ndist:
                    dist[ny][nx] = ndist
                    heapq.heappush(q, [ndist, ny, nx])

    return dist[n-1][n-1]


i = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    print("Problem %d: %d" %(i, dijk(n)))
    i += 1
