import sys
input = sys.stdin.readline

n = int(input())
l = []
ans = -1

for _ in range(n):
    l.append(float(input()))

for i in range(1, n):
    l[i] = max(l[i], l[i] * l[i-1])
    ans = max(ans, l[i])

print("%.3f" %ans)
