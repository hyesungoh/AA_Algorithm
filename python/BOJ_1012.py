from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    pass
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    group = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]


    for _ in range(k):
        y, x = map(int, input().split())
        graph[y][x] = 1

    g_min = 0
    q = deque()
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and visit[y][x] == 0:
                q.append((y,x))
                g_min += 1

                while q:
                    a, b = q.popleft()
                    visit[a][b] = 1
                    group[a][b] = g_min
                    for i in range(4):
                        if 0 <= a + dy[i] < n and 0 <= b + dx[i] < m:
                            if graph[a+dy[i]][b+dx[i]] == 1 and visit[a+dy[i]][b+dx[i]] == 0:
                                q.append((a+dy[i], b+dx[i]))

    print(g_min)
