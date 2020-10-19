# import sys
# input = sys.stdin.readline
#
# n = int(input())
# ans = 0
# l = [[False for _ in range(n)] for _ in range(n)]
#
# def bt(depth):
#     global ans
#
#     if n == depth:
#         ans += 1
#         return
#
#     for i in range(n):
#         for j in range(n):
#             if not l[i][j]:
#                 check_true(l, i, j)
#                 bt(depth+1)
#                 check_false(l, i, j)
#
#
# def check_true(l, i, j):
#     for y in range(n): # 직선 체크
#         if 0 <= y < n:
#             l[y][j] = True
#             l[i][y] = True
#
#         if 0 <= i-y < n and 0 <= j-y < n:
#             l[i - y][j - y] = True
#         if 0 <= i+y < n and 0 <= j+y < n:
#             l[i + y][j + y] = True
#
#
#         if 0 <= i-y < n and 0 <= j+y < n:
#             l[i - y][j + y] = True
#         if 0 <= i+y < n and 0 <= j-y < n:
#             l[i + y][j - y] = True
#
# def check_false(l, i, j):
#     for y in range(n): # 직선 체크
#         if 0 <= y < n:
#             l[y][j] = False
#             l[i][y] = False
#
#         if 0 <= i-y < n and 0 <= j-y < n:
#             l[i - y][j - y] = False
#         if 0 <= i+y < n and 0 <= j+y < n:
#             l[i + y][j + y] = False
#
#         if 0 <= i-y < n and 0 <= j+y < n:
#             l[i - y][j + y] = False
#         if 0 <= i+y < n and 0 <= j-y <n:
#             l[i + y][j - y] = False
#
# bt(0)
# print(ans)

import sys
input = sys.stdin.readline

n = int(input())
ans = 0

st = [False] * n
# 대각선 좌표를 압축하여 저장하기 위해 최대 길이 설장 ex) 3 = 4, 4 = 6, 5 = 8
pl = [False] * (2*n-1)
mi = [False] * (2*n-1)

def bt(depth):
    global ans

    if depth == n:
        ans += 1
        return

    for i in range(n):
        # pl은 오른쪽 위로 향하는 대각선, 왼쪽 위의 인덱스가 0
        # mi는 오른쪽 아래로 향하는 대각선, 오른쪽 위의 인덱스가 0
        if not st[i] and not pl[depth+i] and not mi[depth-i+n-1]:
            st[i] = pl[depth+i] = mi[depth-i+n-1] = True
            bt(depth+1)
            st[i] = pl[depth + i] = mi[depth - i + n - 1] = False

bt(0)
print(ans)
