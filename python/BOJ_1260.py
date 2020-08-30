from collections import deque

def dfs(gra, sta):
    vis = []
    stack = deque([sta])
    while stack:
        nod = stack.pop()
        if nod not in vis:
            vis.append(nod)
            if nod in gra:
                stack.extend(sorted(gra[nod], reverse=True))
    return " ".join(str(i) for i in vis)

def bfs(gra, sta):
    vis = []
    que = deque([sta])
    while que:
        nod = que.popleft()
        if nod not in vis:
            vis.append(nod)
            if nod in gra:
                que.extend(sorted(gra[nod]))

    return " ".join(str(i) for i in vis)

graph = {}
n, m, start = map(int, input().split())
for _ in range(m):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

print(dfs(graph, start))
print(bfs(graph, start))
