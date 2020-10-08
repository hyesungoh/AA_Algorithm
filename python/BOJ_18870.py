# import sys
# input = sys.stdin.readline
# n = int(input())
# l = list(map(int, input().split()))
# sorted_l = sorted(set(l))
#
# d = {}
# for location, i in zip(sorted_l, range(n)):
#     d[location] = i
#
# [print(d[i], end=' ') for i in l]

input()
l = list(map(int, input().split()))
d = {}
for v, k in enumerate(sorted(set(l))): d[k] = v
print(*(d[i] for i in l))
