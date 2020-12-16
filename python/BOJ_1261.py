import sys
import heapq
input = sys.stdin.readline
direc = [[1, 0],
         [-1, 0],
         [0, 1],
         [0, -1]]

def dijkstra():
    visit = [[0 for _ in range(X)] for _ in range(Y)]
    visit[0][0] = 1

    q = []
    heapq.heappush(q, [0, 0, 0])

    while q:
        cnt, y, x = heapq.heappop(q)

        if y == Y-1 and x == X-1:
            return cnt

        for dy, dx in direc:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < Y and 0 <= nx < X and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                if graph[ny][nx] == '1':
                    heapq.heappush(q, [cnt+1, ny, nx])
                else:
                    heapq.heappush(q, [cnt, ny, nx])

X, Y = map(int, input().split())
graph = []
for _ in range(Y):
    graph.append(list(input()))
ans = dijkstra()
print(ans)
