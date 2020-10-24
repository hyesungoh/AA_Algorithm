import sys
input = sys.stdin.readline

l = []; n = int(input())
for _ in range(n):
    l.append(list(map(int, input().split())))

for i in range(n-1, 0, -1):
    for j in range(i):
        l[i-1][j] += max(l[i][j], l[i][j+1])

print(l[0][0])
