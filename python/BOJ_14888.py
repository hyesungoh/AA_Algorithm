# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
#
# def bt(depth, val):
#     global MAX, MIN, visit_op
#
#     if depth == n-1:
#         if val > MAX:
#             MAX = val
#         if val < MIN:
#             MIN = val
#
#         return
#
#     for i in range(n-1):
#         if not visit_op[i]:
#             t_val = str(val) + lop[i] + str(ln[depth + 1])
#             visit_op[i] = True
#             bt(depth+1, int(eval(t_val)))
#
#             visit_op[i] = False
#
#
# n = int(input())
# ln = list(map(int, input().split()))
# t_lop = ['+', '-', '*', '/']
# op = list(map(int, input().split()))
# lop = []
#
# visit_op = [False for _ in range(n)]
# MIN = 100000000
# MAX = -100000000
#
# for i in range(4):
#     [lop.append(t_lop[i]) for _ in range(op[i])]
#
# bt(0, ln[0])
# print(MAX)
# print(MIN)

import sys
input = sys.stdin.readline

def bt(depth, val, p, m, mul, div):
    global MAX, MIN

    if depth == n:
        MAX = max(MAX, val)
        MIN = min(MIN, val)
        return

    if p:
        bt(depth+1, val + l[depth], p-1, m, mul, div)
    if m:
        bt(depth + 1, val - l[depth], p, m - 1, mul, div)
    if mul:
        bt(depth + 1, val * l[depth], p, m, mul - 1, div)
    if div:
        bt(depth+1, -(-val // l[depth]) if val < 0 else val // l[depth], p, m, mul, div - 1)


n = int(input())
l = list(map(int, input().split()))
op = list(map(int, input().split()))

MAX = -1000000001
MIN = 1000000001

bt(1, l[0], op[0], op[1], op[2], op[3])
print(MAX)
print(MIN)
