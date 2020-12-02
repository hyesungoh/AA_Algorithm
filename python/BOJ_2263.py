# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
#
# def getPre(i, l):
#     if i == 0:
#         return
#     num = l.pop()
#     print(num, end=" ")
#
#     index = inor.index(num)
#     visit[index] = True
#
#     next_l = []
#     for node in range(index, n):
#         if not visit[node]:
#             next_l.append(inor[node])
#
#     for node in range(0, index):
#         if not visit[node]:
#             next_l.append(inor[node])
#
#     getPre(i-1, next_l)
#
#
# n = int(input())
# inor = list(map(int, input().split()))
# postor = list(map(int, input().split()))
# visit = [False for _ in range(n)]
# getPre(n, postor)


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def getPre(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    now = postor[post_end]
    print(now, end=" ")
    index = p[now]
    left = post_start + index - in_start
    getPre(in_start, index-1, post_start, left - 1)
    getPre(index+1, in_end, left, post_end-1)


n = int(input())
inor = list(map(int, input().split()))
postor = list(map(int, input().split()))
p = {}
for i in range(n):
    p[inor[i]] = i
getPre(0, n-1, 0, n-1)
