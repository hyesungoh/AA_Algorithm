import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = 0
for i in reversed(l):
    if k >= i:
        ans += k//i
        k %= i
    if k == 0:
        break
print(ans)
