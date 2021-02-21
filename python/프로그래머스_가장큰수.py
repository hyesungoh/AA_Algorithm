# import sys
# sys.setrecursionlimit(10**9)

# def bt(depth, now, length, numbers, visit, answers):
#     if depth == length:
#         answers.append(now)
#         return
#
#     for i in range(length):
#         if not visit[i]:
#             visit[i] = True
#             bt(depth+1, now+numbers[i], length, numbers, visit, answers)
#             visit[i] = False
#
#
# def solution(numbers):
#     n = len(numbers)
#     numbers = list(map(str, numbers))
#     visit = [False for _ in range(n)]
#     answers = []
#     bt(0, "", n, numbers, visit, answers)
#     answers = list(map(int, answers))
#     print(answers)
#     return str(max(answers))


def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return str(int("".join(numbers)))

l = [3, 30, 34, 5, 9]
print(solution(l))
