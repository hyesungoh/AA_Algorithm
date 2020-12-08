import sys
input = sys.stdin.readline

def dfs(sy, sx):
    q = [[sy, sx]]
    check[sy][sx] = True
    cnt = 1
    while q:
        y, x = q.pop()
        for ny, nx in dire:
            next_y = ny + y
            next_x = nx + x
            if 0 <= next_y < Y and 0 <= next_x < X:
                if not check[next_y][next_x]:
                    q.append([next_y, next_x])
                    check[next_y][next_x] = True
                    cnt += 1
    return cnt

dire = [[0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]]

Y, X, k = map(int, input().split())
check = [[False for _ in range(X)] for _ in range(Y)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for vx in range(x1, x2):
        for vy in range(y1, y2):
            check[vy][vx] = True

ans = 0
ans_l = []
for ny in range(Y):
    for nx in range(X):
        if not check[ny][nx]:
            ans_l.append(dfs(ny, nx))
            ans += 1

print(ans)
print(*sorted(ans_l))
