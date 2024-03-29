def solution(part, comp):
    dict = {}
    for per in part:
        if per in dict: dict[per] += 1
        else: dict[per] = 1

    for per in comp: dict[per] -= 1

    for k, v in dict.items():
        if v > 0:
            return k

# def solution(part, comp):
#     part.sort()
#     comp.sort()
#
#     for i in range(len(part)):
#         if part[i] != comp[i]:
#             return part[i]
#     return part[-1]
