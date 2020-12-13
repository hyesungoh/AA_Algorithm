def dfs(start, end):
    q = [[start, 0]]
    while q:
        node, cnt = q.pop()
        visit[node] = True

        if node == end:
            return cnt

        for next in graph[node]:
            if not visit[next]:
                q.append([next, cnt+1])
    return -1

n = int(input())
ans_x, ans_y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = dfs(ans_x, ans_y)
print(ans)
