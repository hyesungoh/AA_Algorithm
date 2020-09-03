n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, list(input()))))
ans = []

def dfs(count, i, j):
    l[i][j] = 0
    if j+1 < n and l[i][j+1] == 1:
        count = dfs(count+1, i, j+1)
    if j-1 >= 0 and l[i][j-1] == 1:
        count = dfs(count+1, i, j-1)
    if i+1 < n and l[i+1][j] == 1:
        count = dfs(count+1, i+1, j)
    if i-1 >= 0 and l[i-1][j] == 1:
        count = dfs(count + 1, i-1, j)

    return count

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            ans.append(dfs(1, i, j))

print(len(ans))
[print(i) for i in sorted(ans)]
