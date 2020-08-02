# l = []
# for i in range(3):
#     l.append(input().split())
#
# x_d, y_d = {}, {}
# for x, y in l:
#     x_d[x] = (2 if x in x_d else 1)
#     y_d[y] = (2 if y in y_d else 1)
#
# for k, v in x_d.items():
#     if v == 1:
#         print(k, end=" ")
#
# for k, v in y_d.items():
#     if v == 1:
#         print(k)

x, y = 0, 0
for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b
print(x, y)
