import sys
INF = -sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
dp1 = [[INF for _ in range(m+1)] for _ in range(n)]
dp2 = [[INF for _ in range(m+1)] for _ in range(n)]

dp1[0][0] = 0
dp2[0][1] = l[0]

for i in range(1, n):
    dp1[i][0] = 0
    dp2[i][0] = INF

    for j in range(1, min(m, (i+2) // 2) + 1):
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp2[i][j] = max(dp1[i-1][j-1] + l[i], dp2[i-1][j] + l[i])

print(max(dp1[n-1][m], dp2[n-1][m]))
