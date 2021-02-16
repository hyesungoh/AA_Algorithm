n = int(input())
l = list(map(int, input().split()))
pdp = [1 for _ in range(n)]
ndp = [1 for _ in range(n)]

for i in range(1, n):
    if l[i] >= l[i-1]: pdp[i] = pdp[i-1] + 1
    if l[i] <= l[i-1]: ndp[i] = ndp[i-1] + 1

print(max(max(pdp), max(ndp)))
