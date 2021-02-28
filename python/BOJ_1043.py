import sys
input = sys.stdin.readline

def find(node):
    if parents[node] == node:
        return node

    p = find(parents[node])
    parents[node] = p
    return p

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        if know[pa] or know[pb]:
            know[pa], know[pb] = True, True

        if pb < pa:
            parents[pa] = pb
        else:
            parents[pb] = pa

n, m = map(int, input().split())
parents = [i for i in range(n+1)]
know = [False for i in range(n+1)]
party = []
ans = 0

know_input = list(map(int, input().split()))
for t in know_input[1:]:
    know[t] = True


for _ in range(m):
    p = list(map(int, input().split()))
    party.append(p)

    for i in range(1, p[0]):
        union(p[i], p[i+1])

for i in range(m):
    member = party[i][0]
    for j in range(1, member+1):
        pj = find(party[i][j])
        if know[pj]: break
        if not know[pj] and j == member: ans += 1

print(ans)
