from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
check = [[False]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]

que = deque()

que.append((0, 0))
dist[0][0] = 1
check[0][0] = True

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while que:
    i, j = que.popleft()
    for temp in range(4):
        x = dx[temp] + i
        y = dy[temp] + j
        if 0 <= x < n and 0 <= y < m:
            if check[x][y] is False and graph[x][y] == 1:
                que.append((x, y))
                dist[x][y] = dist[i][j] + 1
                check[x][y] = True
print(dist[n-1][m-1])
