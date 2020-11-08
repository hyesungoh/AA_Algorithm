# 1339
# n = int(input())
# l = [[0 for _ in range(10)] for _ in range(n)]
# d = {}
# index = 9
#
# for i in range(n):
#     s = input()
#     ls = len(s)
#     for j in range(ls):
#         l[i][ls-j-1] = s[j]
#
# for i in range(9, -1, -1):
#     for y in range(n):
#         if l[y][i] != 0 and l[y][i] not in d:
#             d[l[y][i]] = index
#             l[y][i] = index
#
#             index -= 1
#         elif l[y][i] in d:
#             l[y][i] = d[l[y][i]]
#
# ans = 0
# for i in range(n):
#     rev_l = list(reversed(l[i]))
#     s = ''.join(map(str, rev_l))
#     ans += int(s)
#
# print(ans)

n = int(input())
l = []; ans = 0
alpha = [0 for _ in range(26)]

for _ in range(n):
    l.append(input())

for s in l:
    i = 0
    while s:
        now = s[-1]
        alpha[ord(now) - ord('A')] += pow(10, i)
        i += 1; s = s[:-1]

alpha.sort(reverse=True)
for i in range(9, 0, -1):
    ans += alpha[9-i] * i
print(ans)
