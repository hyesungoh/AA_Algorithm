import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]


for _ in range(m):
    s, e, w = map(int, input().split())
    dist[s][e] = min(dist[s][e], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        dist[i][i] = 0
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        ans = dist[i][j] if dist[i][j] != INF else 0
        print(ans, end=" ")
    print()
