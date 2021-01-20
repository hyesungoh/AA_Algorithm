import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

dire = [[1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]]

def solve(n, graph):
    q = []
    # cnt, y, x
    heapq.heappush(q, [0, 0, 0])
    dist = [[INF for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0

    while q:
        cnt, y, x = heapq.heappop(q)

        for dy, dx in dire:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if cnt + 1 < dist[ny][nx]:
                    if graph[ny][nx] == 0:
                        heapq.heappush(q, [cnt + 1, ny, nx])
                        dist[ny][nx] = cnt + 1
                    else:
                        heapq.heappush(q, [cnt, ny, nx])
                        dist[ny][nx] = cnt
    return dist[n-1][n-1]

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().strip()))

print(solve(n, graph))
