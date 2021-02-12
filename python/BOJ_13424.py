import sys
INF = sys.maxsize
input = sys.stdin.readline

def floyd():
    for k in range(1, N+1):
        graph[k][k] = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    K = int(input())
    start = list(map(int, input().split()))
    floyd()

    values = [0 for _ in range(N+1)]
    values[0] = INF
    min_value = INF

    for node in range(1, N + 1):
        for person in start:
            values[node] += graph[person][node]
        min_value = min(min_value, values[node])

    print(values.index(min_value))
