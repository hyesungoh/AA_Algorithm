# l = []
# for _ in range(int(input())):
#     l.append(int(input()))
# l.sort(reverse=True)
# [print(i) for i in l]

# import sys
# print(*sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse = True))

import sys
input = sys.stdin.readline
l = []
for _ in range(int(input())):
    l.append(int(input()))
[print(i) for i in sorted(l, reverse=True)]
