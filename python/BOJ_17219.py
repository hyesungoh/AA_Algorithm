import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
    s, p = input().split()
    d[s] = p

for _ in range(m):
    print(d[input().strip()])
