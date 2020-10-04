# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def bfs():
#     pass
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# for _ in range(int(input())):
#     n, m, k = map(int, input().split())
#     graph = [[0 for _ in range(m)] for _ in range(n)]
#     group = [[0 for _ in range(m)] for _ in range(n)]
#     visit = [[0 for _ in range(m)] for _ in range(n)]
#
#
#     for _ in range(k):
#         y, x = map(int, input().split())
#         graph[y][x] = 1
#
#     g_min = 0
#     q = deque()
#     for y in range(n):
#         for x in range(m):
#             # 1이며 방문한 적이 없을 때
#             if graph[y][x] == 1 and visit[y][x] == 0:
#                 # 큐에 추가
#                 q.append((y,x))
#                 # 그룹 넘버 + 1
#                 g_min += 1
#
#                 # 연결된 정점들이 없을 때 까지
#                 while q:
#                     a, b = q.popleft()
#                     visit[a][b] = 1
#                     group[a][b] = g_min
#
#                     # 상하좌우 확인
#                     for i in range(4):
#                         if 0 <= a + dy[i] < n and 0 <= b + dx[i] < m:
#                             if graph[a+dy[i]][b+dx[i]] == 1 and visit[a+dy[i]][b+dx[i]] == 0:
#                                 q.append((a+dy[i], b+dx[i]))
#
#     print(g_min)


from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(start, graph):
    q = deque()
    q.append(start)

    while q:
        a, b = q.popleft()
        graph[a][b] = 0
        for i in range(4):
            n_y = a + dy[i]
            n_x = b + dx[i]
            if 0 <= n_y < y and 0 <= n_x < x and graph[n_y][n_x] == 1:
                q.append((n_y, n_x))
                graph[n_y][n_x] = 0
    return 1

for _ in range(int(input())):
    y, x, k = map(int, input().split())
    graph = [[0 for _ in range(x)] for _ in range(y)]

    for _ in range(k):
        t_y, t_x = map(int, input().split())
        graph[t_y][t_x] = 1

    count = 0
    for i in range(y):
        for j in range(x):
            if graph[i][j] == 1:
                count += bfs((i,j), graph)

    print(count)
