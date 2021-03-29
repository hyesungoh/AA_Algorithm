n = int(input())
l = list(map(int, input().split()))
upper = [1 for _ in range(n)]
downer = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            upper[i] = max(upper[i], upper[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if l[i] > l[j]:
            downer[i] = max(downer[i], downer[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, upper[i] + downer[i] - 1)

print(answer)
