import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
l_add = [0]

for i in range(n): l_add.append(l_add[-1] + l[i])
for _ in range(m):
    i, j = map(int, input().split())
    print(l_add[j] if i == 1 else l_add[j] - l_add[i-1])
