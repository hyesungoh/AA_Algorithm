# 1254
def ispalin(s):
    len_s = len(s)
    for i in range(len_s // 2):
        if s[i] != s[len_s-i-1]:
            return False
    return True

s = input()

if ispalin(s):
    print(len(s))
    exit(0)

for i in range(len(s)):
    t = s + ''.join(reversed(s[0:i+1]))

    if ispalin(t):
        print(len(t))
        exit(0)

# s = input()
# n = len(s)
# for i in range(n):
#     if s[i:] in s[i:][::-1]:
#         print(n + i)
#         break
