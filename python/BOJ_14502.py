import sys
input = sys.stdin.readline

dist = [[0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]]

def count_safezone(graph):
    global ans
    cnt = 0
    for y in range(Y):
        for x in range(X):
            if graph[y][x] == 0:
                cnt += 1
    ans = max(ans, cnt)

def infection(graph):
    temp_graph = [[0 for _ in range(X)] for _ in range(Y)]
    q = []

    for y in range(Y):
        for x in range(X):
            temp_graph[y][x] = graph[y][x]
            if temp_graph[y][x] == 2:
                q.append([y, x])

    while q:
        y, x = q.pop()
        for dy, dx in dist:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < Y and 0 <= nx < X:
                if temp_graph[ny][nx] == 0:
                    temp_graph[ny][nx] = 2
                    q.append([ny, nx])
    count_safezone(temp_graph)

def create_wall(depth):
    if depth == 3:
        infection(graph)
        return

    for y in range(Y):
        for x in range(X):
            if graph[y][x] == 0:
                graph[y][x] = 1
                create_wall(depth+1)
                graph[y][x] = 0


Y, X = map(int, input().split())
graph = [[] for _ in range(Y)]
for i in range(Y):
    graph[i] = list(map(int, input().split()))
ans = 0
create_wall(0)

print(ans)
