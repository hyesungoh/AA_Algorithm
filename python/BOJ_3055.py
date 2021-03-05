import sys
from collections import deque
input = sys.stdin.readline

dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def water_move(wdist):
    while water:
        y, x = water.popleft()
        now_value = wdist[y][x]

        for ty, tx in dire:
            ny, nx = y + ty, x + tx
            if 0 <= ny < Y and 0 <= nx < X:
                if wdist[ny][nx] > now_value + 1 and graph[ny][nx] == ".":
                    wdist[ny][nx] = now_value + 1
                    water.append([ny, nx])

def dochi_move(dist):
    while dochi:
        y, x = dochi.popleft()
        now_value = dist[y][x]

        for ty, tx in dire:
            ny, nx = y + ty, x + tx
            if 0 <= ny < Y and 0 <= nx < X:
                if wdist[ny][nx] > now_value + 1and (graph[ny][nx] == "." or graph[ny][nx] == "D"):
                    if dist[ny][nx] > now_value + 1:
                        dist[ny][nx] = now_value + 1
                        dochi.append([ny, nx])

Y, X = map(int, input().split())
graph = [list(input()) for _ in range(Y)]

wdist = [[X*Y for _ in range(X)] for _ in range(Y)]
dist = [[X*Y for _ in range(X)] for _ in range(Y)]
water = deque()
dochi = deque()

for y in range(Y):
    for x in range(X):
        if graph[y][x] == '*':
            water.append([y, x])
            wdist[y][x] = 0
        elif graph[y][x] == 'S':
            dochi.append([y, x])
            dist[y][x] = 0
        elif graph[y][x] == 'D':
            endY, endX = y, x

water_move(wdist)
dochi_move(dist)

print("KAKTUS" if dist[endY][endX] == Y * X else dist[endY][endX])
