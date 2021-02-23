import sys
input = sys.stdin.readline

n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
ans = 0

for _ in range(n):
    y, x = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):

            if not paper[i][j]:
                paper[i][j] = 1
                ans += 1

print(ans)
