# import sys
# input = sys.stdin.readline
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     is_all_negative = True
#     l = [0 for _ in range(n)]
#     dp = [0 for _ in range(n)]
#     for i in range(n):
#         t = int(input())
#         if t > 0:
#             is_all_negative = False
#
#         l[i] = t
#         dp[i] = t
#
#     if is_all_negative:
#         print(max(l))
#         continue
#
#
#     for i in range(1, n):
#         for j in range(i):
#             dp[i] = max(l[i], dp[i] + l[j])
#
#     print(max(dp))


# import math
#
# def init(node, start, end):
#     global ans
#     if start == end:
#         tree[node] = l[start]
#         ans = max(ans, tree[node])
#         return tree[node]
#
#     mid = (start + end) // 2
#     tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
#     ans = max(ans, tree[node])
#     return tree[node]
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     l = [0 for _ in range(n)]
#     for i in range(n):
#         l[i] = int(input())
#
#     height = math.ceil(math.log2(n))
#     size = 2 ** (height + 1)
#     tree = [0 for _ in range(size)]
#
#     ans = -10001
#     init(1, 0, n-1)
#     print(ans)

# import sys
# input = sys.stdin.readline
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     l = [0 for _ in range(n)]
#     for i in range(n):
#         l[i] = int(input())
#
#     max_sum = cur_sum = 0
#     max_start = max_end = -1
#     cur_start = 0
#     for index, value in enumerate(l):
#         if cur_sum <= 0:
#             cur_start = index
#             cur_sum = value
#         else:
#             cur_sum += value
#
#         if cur_sum > max_sum:
#             max_sum = cur_sum
#             max_start = cur_start
#             max_end = index + 1
#
#     if max_end == -1:
#         max_sum = l[0]
#         for i in range(1, n):
#             max_sum = max(max_sum, l[i])
#
#     print(max_sum)

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    l = [0 for _ in range(n)]
    dp = [-10001 for _ in range(n)]

    for i in range(n):
        l[i] = int(input())

    dp[0] = l[0]
    for i in range(n):
        dp[i] = max(dp[i-1] + l[i], l[i])
    print(max(dp))
