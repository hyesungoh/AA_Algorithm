import sys
input = sys.stdin.readline

n = int(input())
l = sorted([int(input()) for _ in range(n)])

for i in range(n):
    l[i] = l[i] * (n-i)
print(max(l))
