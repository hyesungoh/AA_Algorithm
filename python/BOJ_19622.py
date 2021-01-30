import sys
input = sys.stdin.readline

n = int(input())
l = [0 for _ in range(n)]
for i in range(n):
    s, e, w = map(int, input().split())
    l[i] = w

if n <= 2:
    print(max(l))
    exit(0)

l[2] += l[0]
for i in range(3, n):
    l[i] = max(l[i-2], l[i-3]) + l[i]

print(max(l))
