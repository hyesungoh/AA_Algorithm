# def KMP(t, p, lps):
#     lt = len(t)
#     lp = len(p)
#     ans = 0
#     i = 0
#     j = 0
#     while i < lt:
#         if t[i] == p[j]:
#             i += 1
#             j += 1
#         elif t[i] != p[j]:
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1
#
#         if j == lp:
#             ans += 1
#             if ans >= 2:
#                 return True
#             j = lps[j-1]
#     return False
#
# def getLPS(p, lps):
#     leng = 0
#     i = 1
#
#     while i < len(p):
#         if p[i] == p[leng]:
#             leng += 1
#             lps[i] = leng
#             i += 1
#         else:
#             if leng != 0:
#                 leng = lps[leng-1]
#             else:
#                 lps[i] = 0
#                 i += 1
#
# s = input()
# ls = len(s)
# for i in range(ls-1, 1, -1):
#     pat = s[0:i]
#     lps = [0 for _ in range(i)]
#     getLPS(pat, lps)
#     if KMP(s, pat, lps):
#         print(i)
#         break


def getLpsMax(p):
    lps = [0 for _ in range(len(p))]
    leng = 0
    i = 1

    while i < len(p):
        if p[i] == p[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1
    return max(lps)

s = input()
ls = len(s)
ans = 0
for i in range(ls):
    p = s[i:ls]
    ans = max(getLpsMax(p), ans)
print(ans)
