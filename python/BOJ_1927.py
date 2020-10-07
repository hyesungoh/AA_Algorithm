# from bisect import insort
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# l = deque()
# for _ in range(int(input())):
#     s = int(input())
#     if s > 0:
#         insort(l, s)
#     else:
#         if l == []:
#             print('0')
#         else:
#             print(l.popleft())


import sys, heapq
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    n = int(input())
    if n > 0:
        heapq.heappush(h, n)
    else:
        if h == []:
            print(0)
        else:
            print(heapq.heappop(h))
