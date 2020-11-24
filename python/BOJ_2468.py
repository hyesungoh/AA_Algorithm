import sys
input = sys.stdin.readline

dire = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

def dfs(y, x, i):
    q = [[y, x]]

    while q:
        hy, hx = q.pop()
        visit[hy][hx] = True

        for ny, nx in dire:
            next_y, next_x = ny + hy, nx + hx
            if 0 <= next_y < n and 0 <= next_x < n:
                if graph[next_y][next_x] > i and not visit[next_y][next_x]:
                    q.append([next_y, next_x])


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = 1
for i in range(1, 101):
    cnt = 0
    visit = [[False for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if graph[y][x] > i and not visit[y][x]:
                dfs(y, x, i)
                cnt += 1
    if cnt == 0:
        break
    if ans <= cnt:
        ans = cnt
print(ans)
