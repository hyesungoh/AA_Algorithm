# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# l = []
# for _ in range(n):
#     l.append(list(map(int, input().split())))
#
# for _ in range(m):
#     ans = 0
#     y1, x1, y2, x2 = map(int, input().split())
#     for y in range(y1-1, y2):
#         for x in range(x1-1, x2):
#             ans += l[y][x]
#     print(ans)
#
# O(n^2)라 시간초과


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
l_add = [[0] for _ in range(n)]

# 2차원 배열 입력
for _ in range(n): l.append(list(map(int, input().split())))

# 누적합 계산
for i in range(n):
    for j in range(n):
        l_add[i].append(l_add[i][-1] + l[i][j])

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    ans = 0
    for i in range(y1-1, y2):
        ans += l_add[i][x2] if x1 == 1 else l_add[i][x2] - l_add[i][x1-1]

    print(ans)
