# 문자열을 list로 만들어서 접
# s = input()
# t = ""
# for w in list(s):
#     t += w
#     if w is '>':
#         print(t, end="")
#         t = ""
#     elif '<' not in t and w == ' ':
#         # print(''.join(reversed(t)), end="")
#         print(t)
#         t = ""
#     elif w is None:
#         print("afff")

# 문자열 split으로 접근
# s = input().split()
# t = ""
# for w in s:
#     if '>' in w:
#         t += w
#         print(t, end="")
#         t = ""
#     elif '<' in w:
#         t += w
#     else:
#         print(''.join(reversed(w)), end="")

s = list(input())
t = ""
s.append(' ')

for w in s:
    if w is '<':
        print(''.join(reversed(t)), end='')
        t = '<'
    elif w is '>':
        t += '>'
        print(t, end='')
        t = ''
    elif w is ' ' and '<' not in t:
        print(''.join(reversed(t)), end='')
        print(' ', end='')
        t = ''
    else:
        t += w
