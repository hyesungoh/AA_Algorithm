# 5555
# import sys
# input = sys.stdin.readline
#
# s = input()[0:-1]
# ans = 0
# for _ in range(int(input())):
#     l = input()[0:-1] * 2
#     if s in l: ans += 1
# print(ans)

s = input()
ans = 0
for _ in range(int(input())):
    l = input() * 2
    if s in l: ans += 1
print(ans)
