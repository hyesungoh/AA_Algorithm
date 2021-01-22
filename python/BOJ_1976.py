import sys
input = sys.stdin.readline

def solve():
    for i in range(m - 1):
        now = dist[i]
        next = dist[i + 1]
        if not graph[now][next]:
            return False
    return True

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    graph[k][k] = 1
    for i in range(n):
        for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

dist = list(map(lambda x: int(x)-1, input().split()))

print("YES" if solve() else "NO")
