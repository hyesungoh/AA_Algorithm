import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(graph, start):
    q = deque([[start, 0]])
    visit = [False for _ in range(len(graph)+1)]
    visit[start] = True
    max_value = 0
    max_node = 0

    while q:
        node, weight = q.popleft()
        if max_value < weight:
            max_value = weight
            max_node = node

        for next in graph[node]:
            if not visit[next[0]]:
                visit[next[0]] = True
                q.append([next[0], weight + next[1]])

    return max_node, max_value

n = int(input())
graph = {}
for _ in range(n):
    l = list(map(int, input().split()))
    start = l[0]
    for i in range(1, len(l)-1, 2):
        if start not in graph:
            graph[start] = [[l[i], l[i+1]]]
        else:
            graph[start].append([l[i], l[i+1]])

mn, mv = dijkstra(graph, 1)
print(dijkstra(graph, mn)[1])
