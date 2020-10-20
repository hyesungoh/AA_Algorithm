import sys
input = sys.stdin.readline

i, j = map(int, input().split())
ans = 0

s = {input().strip() for _ in range(i)}

for _ in range(j):
    if input().strip() in s:
        ans += 1

print(ans)
