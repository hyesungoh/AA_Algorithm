Y, X = map(int, input().split())
graph = [[] for _ in range(Y)]
for i in range(Y): graph[i] = list(map(int, input()))
ans = 0 if graph[0][0] == 0 else 1

for y in range(1, Y):
    for x in range(1, X):
        if graph[y][x] != 1:
            continue
        min_value = min(graph[y-1][x], graph[y][x-1], graph[y-1][x-1])
        graph[y][x] = min_value + 1
        ans = max(ans, graph[y][x])

print(ans*ans)
