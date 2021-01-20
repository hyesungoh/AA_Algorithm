# s = input()
# k = input()
#
# no_num_s = []
# for i in s:
#     if not i.isdigit():
#         no_num_s.append(i)
# no_num_s = "".join(no_num_s)
#
# print(1 if k in no_num_s else 0)

s = input()
k = input()
for i in "0123456789":
    s = s.replace(i, "")
print(1 if k in s else 0)
