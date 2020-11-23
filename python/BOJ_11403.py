def dfs(start):
    q = [start]
    v = [0 for _ in range(n)]

    while q:
        here = q.pop()
        for i in range(n):
            if graph[here][i] == 1 and v[i] == 0:
                v[i] = 1
                q.append(i)
    return v


n = int(input())
graph = [[] for _ in range(n)]
visit = []
for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    temp = dfs(i)
    visit.append(temp)

[print(*i) for i in visit]
