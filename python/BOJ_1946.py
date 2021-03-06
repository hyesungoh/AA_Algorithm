# import sys
# input = sys.stdin.readline
#
# for _ in range(int(input())):
#     n = int(input())
#     l = []
#     for _ in range(n): l.append(list(map(int, input().split())))
#     l.sort()
#
#     cnt = 0
#     m = l[0][1]
#     for i in range(1, n):
#         if m > l[i][1]:
#             m = l[i][1]
#         else:
#             cnt += 1
#
#     print(n-cnt)


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = [0 for _ in range(n)]
    for _ in range(n):
        a, b = map(int, input().split())
        l[a-1] = b

    cnt = 0
    m = l[0]
    for i in range(1, n):
        if m > l[i]: m = l[i]
        else: cnt += 1

    print(n-cnt)
