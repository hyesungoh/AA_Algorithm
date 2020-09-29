import sys
input = sys.stdin.readline

n = int(input())
graph = [input().split() for _ in range(n)]
count = [0, 0]

def isunity(x, y, size):
    global count
    color = graph[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != color:
                isunity(x, y, size//2)
                isunity(x, y + size//2, size//2)
                isunity(x + size//2, y, size//2)
                isunity(x + size//2, y + size//2, size//2)
                return
    count[int(color)] += 1

isunity(0, 0, n)
[print(i) for i in count]
