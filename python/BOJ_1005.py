
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())

    times = [0] + list(map(int, input().split()))
    answers = [0] + times[1:]

    tree = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]

    for _ in range(K):
        bef, nex = map(int, input().split())
        tree[bef].append(nex)
        indegree[nex] += 1

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i]

    while q:
        now = q.popleft()

        for next in tree[now]:
            indegree[next] -= 1
            answers[next] = max(answers[next], answers[now] + times[next])
            if indegree[next] == 0:
                q.append(next)

    print(answers[int(input())])Î
