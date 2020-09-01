def dfs(graph):
    visit = []
    stack = [1]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph:
                stack.extend(graph[node])
    return visit

graph = {}
input()
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

print(len(dfs(graph))-1)
