from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)] # 트리
indegree = [0 for _ in range(n+1)] # 진입차수

for _ in range(m):
    small, big = map(int, input().split())
    tree[small].append(big)
    indegree[big] += 1 # 진입차수 추가

q = deque()
ans = [] # 정답

for i in range(1, n+1):
    if indegree[i] == 0: # 진입차수가 0인 (제일 작은) 정점 추가
        q.append(i)

while q:
    now = q.popleft()
    ans.append(now)
    for next in tree[now]: # 현재 노드보다 큰 정점들
        indegree[next] -= 1 # 해동 노드의 진입차수를 줄임
        if indegree[next] == 0: # 줄였을 때 0일 시, 큐에 추가
            q.append(next)

print(*ans)
