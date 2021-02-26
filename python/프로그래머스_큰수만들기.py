# def bt(n, depth, k, visit, answer, answers):
#     if depth == k:
#         t = "".join(answer)
#         answers.add(int(t))
#         return
#
#     for i in range(n):
#         if not visit[i]:
#             t = answer[i]
#             answer[i] = ""
#             visit[i] = True
#
#             bt(n, depth+1, k, visit, answer, answers)
#
#             answer[i] = t
#             visit[i] = False
#
# def solution(number, k):
#     n = len(number)
#     number = list(number)
#     visit = [False for _ in range(n)]
#     answers = set()
#     bt(n, 0, k, visit, number, answers)
#     return str(max(answers))
#
# print(solution(n, k))


nn = "4177252841"
k = 4

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)

    if k != 0: stack = stack[:-k]
    return "".join(stack)

print(solution(nn, k))
