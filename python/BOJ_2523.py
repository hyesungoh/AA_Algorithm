# 2523
# x = int(input())
# l = list(range(1, x)) + list(range(x, 0, -1))
# if x == 1:
#     print("*")
# else:
#     for i in l:
#         print("*" * i)

n = int(input())
for i in range(n-1, -n, -1):
    print("*" * (n-abs(i)))
