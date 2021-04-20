# n = int(input())
# l = list(map(int, input().split()))
# dp = [1 for _ in range(n)]
# ans = 0
#
# for i in range(n):
#     for j in range(0, i):
#         if l[i] > l[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#     ans = max(dp[i], ans)
#
# print(ans)

# def lower_bound(length, value):

#     for i in range(length):
#         if vt[i] == value:
#             return

#         elif vt[i] > value:
#             vt[i] = value
#             return

#     if vt[0] > value:
#         vt[0] = value
#         return

# n = int(input())
# l = list(map(int, input().split()))
# vt = [0 for _ in range(n)]
# vt[0] = l[0]

# ans = 0

# for i in range(n):
#     if vt[ans] < l[i]:
#         ans += 1
#         vt[ans] = l[i]
#     else:
#         lower_bound(ans+1, l[i])

# print(ans+1)


import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
stack = [0]

for i in l:
    if stack[-1] < i: stack.append(i)
    else: stack[bisect_left(stack, i)] = i

print(len(stack)-1)