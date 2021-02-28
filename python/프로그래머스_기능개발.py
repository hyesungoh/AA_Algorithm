# def solution(pgrs, spds):
#     n = len(pgrs)
#     days = 1
#     last_days = [0]
#     ans = []
#
#     for i in range(n):
#         while True:
#             if pgrs[i] + days * spds[i] >= 100:
#                 if last_days[-1] == days:
#                     ans[-1] += 1
#                 else:
#                     last_days.append(days)
#                     ans.append(1)
#                 break
#
#             days += 1
#
#     return ans


from collections import deque

def solution(pgrs, spds):
    pgrs = deque(pgrs)
    spds = deque(spds)
    answer = []
    days, count = 0, 0

    while pgrs:
        if pgrs[0] + days * spds[0] >= 100:
            pgrs.popleft()
            spds.popleft()
            count += 1
        else:
            days += 1
            if count > 0:
                answer.append(count)
                count = 0

    answer.append(count)
    return answer
