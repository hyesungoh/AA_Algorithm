from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
times = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]

for i in range(1, n+1):
    inputs = list(map(int, input().split()))
    times[i] = inputs[0]
    answer[i] = inputs[0]

    if inputs[1] == -1:
        continue
    for before in inputs[1:]:
        if before == -1: break
        tree[before].append(i)
        inDegree[i] += 1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for next in tree[now]:
        inDegree[next] -= 1
        answer[next] = max(answer[next], answer[now] + times[next])
        if inDegree[next] == 0:
            q.append(next)

[print(ans) for ans in answer[1:]]
