from collections import deque
que = deque()

n, m = map(int, input().split())

graph = []
check = [[False] * n for _ in range(m)]
dist = [[0] * n for _ in range(m)]
isnone = True

for y in range(m):
    graph.append(list(map(int, input().split())))
    for x in range(n):
        if graph[y][x] == 1:
            que.append((y, x))
            check[y][x] = True
            dist[y][x] = 0
            isnone = False

if isnone == True:
    print(-1)
    exit(0)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while que:
    i, j = que.popleft()

    for temp in range(4):
        x = dx[temp] + i
        y = dy[temp] + j
        if 0 <= y < n and 0 <= x < m:
            if check[x][y] == False and graph[x][y] == 0:
                que.append((x, y))
                dist[x][y] = dist[i][j] + 1
                check[x][y] = True
                graph[x][y] = 1

day = 0
for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            print(-1)
            exit(0)
        if dist[y][x] > day:
            day = dist[y][x]
print(day)
