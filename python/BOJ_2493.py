# n = int(input())
# l = list(map(int, input().split()))
# rec = [0 for _ in range(n)]
#
# for i in range(n-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if l[i] <= l[j]:
#             rec[i] = j+1
#             break
# print(*rec)
#
# def solve(check_id, cur_id):
#     if 0 <= check_id < n and 0 <= cur_id < n:
#         if l[check_id] >= l[cur_id]:
#             rec[cur_id] = check_id+1
#         return
#     if check_id > 0:
#         solve(check_id-1, cur_id)
#
# n = int(input())
# l = list(map(int, input().split()))
# rec = [0 for _ in range(n)]
#
# for i in range(1, n):
#     solve(i-1, i)
#
# print(*rec)

n = int(input())
l = list(map(int, input().split()))

value_stack = []
index_stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while value_stack:
        if value_stack[-1] > l[i]:
            answer[i] = index_stack[-1] + 1
            break
        else:
            value_stack.pop()
            index_stack.pop()

    value_stack.append(l[i])
    index_stack.append(i)

print(*answer)
