# def solution(name):
#     def isAllZero(start, end):
#         for i in range(start, end):
#             if changes[i] != 0: return False
#         return True
#
#     length = len(name)
#     changes = [0 for _ in range(length)]
#     for i in range(length):
#         n = ord(name[i])
#         t1 = n - 65
#         t2 = abs(90 - n + 1)
#         changes[i] = min(t1, t2)
#     s = sum(changes)
#
#     search_left = 0
#     for i in range(length):
#         if isAllZero(i, length): break
#         search_left += 1
#
#     search_right = 0
#     for i in range(length, -1, -1):
#         if isAllZero(1, i): break
#         search_right += 1
#
#     print(s)
#     print(search_left)
#     print(search_right)
#     return min(search_left, search_right) + s
#
#     # print(ord("A")) 65
#     # print(ord("X")) 90
#
# n = "BBAAAAAAAAB"
# print(solution(n))


def solution(name):
    length = len(name)
    changes = [0 for _ in range(length)]
    for i in range(length):
        n = ord(name[i])
        t1 = n - 65
        t2 = abs(90 - n + 1)
        changes[i] = min(t1, t2)

    index = 0
    answer = 0
    while True:
        answer += changes[index]
        changes[index] = 0
        if sum(changes) == 0: return answer

        left, right = 1, 1
        while changes[index - left] == 0:
            left += 1
        while changes[index + right] == 0:
            right += 1
        answer += left if left < right else right
        index += -left if left < right else right
