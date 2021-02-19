import sys
input = sys.stdin.readline

dire = [[1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]]


def dfs(sy, sx, color, tgraph, tvisit):
    q = [[sy, sx]]
    tvisit[sy][sx] = True

    while q:
        y, x = q.pop()
        for ty, tx in dire:
            ny, nx = y + ty, x + tx
            if 0 <= ny < n and 0 <= nx < n:
                if not tvisit[ny][nx] and tgraph[ny][nx] == color:
                    q.append([ny, nx])
                    tvisit[ny][nx] = True

n = int(input())
graph = [[] for _ in range(n)]
colorweekgraph = [[] for _ in range(n)]

for i in range(n):
    t = input()
    graph[i] = list(t)
    colorweekgraph[i] = list(map(lambda x: 'R' if x == 'G' else x, t))

visit = [[False for _ in range(n)] for _ in range(n)]
colorweekvisit = [[False for _ in range(n)] for _ in range(n)]

area, colorweekarea = 0, 0
for y in range(n):
    for x in range(n):
        if not visit[y][x]:
            dfs(y, x, graph[y][x], graph, visit)
            area += 1
        if not colorweekvisit[y][x]:
            dfs(y, x, colorweekgraph[y][x], colorweekgraph, colorweekvisit)
            colorweekarea +=1

print(area, colorweekarea)
