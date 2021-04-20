import sys
input = sys.stdin.readline

def dfs(start):
    if visit[start] == 1: return 0

    visit[start] = 1
    for i in S[start]:
        if E[i] == 0 or dfs(E[i]):
            E[i] = start
            return 1
    return 0

N, M = map(int, input().split())
S = [[] for _ in range(N+1)]
E = [0 for _ in range(M+1)]
ans = 0

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    S[i].extend(temp[1:])

for i in range(1, N+1):
    visit = [0 for _ in range(N+1)]
    if dfs(i): ans += 1

print(ans)