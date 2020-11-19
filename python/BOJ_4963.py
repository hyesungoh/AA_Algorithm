import sys
input = sys.stdin.readline

dire = [
    [1, 0],
    [-1, 0],
    [0, -1],
    [0, 1],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
]

def dfs(hy, hx):
    global land

    visit[hy][hx] = True
    q = [[hy, hx]]

    while q:
        ty, tx = q.pop()
        for ny, nx in dire:
            next_y, next_x = ty+ny, tx+nx
            if 0 <= next_y < y and 0 <= next_x < x:
                if visit[next_y][next_x] == False and graph[next_y][next_x] == 1:
                    visit[next_y][next_x] = True
                    graph[next_y][next_x] = land
                    q.append([next_y, next_x])


while True:
    x, y = map(int, input().split())
    if x == 0:
        break

    graph = []
    for _ in range(y):
        graph.append(list(map(int, input().split())))

    visit = [[False for _ in range(x)] for _ in range(y)]
    land = 0

    for ty in range(y):
        for tx in range(x):
            if visit[ty][tx] == False and graph[ty][tx] == 1:
                dfs(ty, tx)
                land += 1
    print(land)
