# 2193
# n = int(input())
# if n <= 2:
#     print(1)
#     exit(0)
#
# first = ('1' + ('0' * (n-1)))
# s = {first}
#
# for i in range(n-1, 1, -1):
#     temp = list(first)
#     if temp[i - 1] == '0':
#         temp[i] = '1'
#         s.add(''.join(temp))
#
#     for j in range(n-1, i-1, -1):
#         if temp[j - 1] == '0':
#             temp[j] = '1'
#             s.add(''.join(temp))
#             temp[j] = '0'
#             continue
# print(len(s))

def f(n):
    if n <= 2:
        return 1
    o, t = 1, 1
    for _ in range(n-2):
        temp = o + t
        o = t
        t = temp
    return temp


n = int(input())
print(f(n))
