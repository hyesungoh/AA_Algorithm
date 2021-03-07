import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]

for _ in range(m):
    before, after = map(int, input().split())
    tree[before].append(after)
    inDegree[after] += 1

q = []
for i in range(1, n+1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

ans = []
while q:
    now = heapq.heappop(q)
    ans.append(now)

    for next in tree[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            heapq.heappush(q, next)

print(*ans)
