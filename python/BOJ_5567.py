def bfs():
    que = []
    visit = set(graph[1])
    que.extend(graph[1])
    for i in que:
        for j in graph[i]:
            visit.add(j)
    return visit

input()
n = int(input())
graph = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

print(len(bfs())-1)
