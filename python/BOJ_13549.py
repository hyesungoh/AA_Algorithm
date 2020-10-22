from collections import deque

n, k = map(int, input().split())
q = deque([[n, 0]])
visit = [False] * 100001

while q:
    loca, sec = q.popleft()
    if loca == k:
        print(sec)
        exit(0)

    if not visit[loca]:
        visit[loca] = True
        t = [loca*2, loca+1, loca-1]

        if 0 <= t[0] <= 100000:
            q.appendleft([loca*2, sec])
        if 0 <= t[1] <= 100000:
            q.append([loca+1, sec+1])
        if 0 <= t[2] <= 100000:
            q.append([loca-1, sec+1])

# from collections import deque
#
# def f(n, k):
#     q = deque([[n, 0]])
#     while q:
#         loca, sec = q.popleft()
#         if loca == k:
#             return sec
#         for i in [loca*2, loca+1, loca-1]:
#             if 0 <= i <= 100000 and not visit[i]:
#                 if i == loca*2 and i != 0:
#                     q.appendleft([i, sec])
#                 else:
#                     q.append([i, sec+1])
#
# n, k = map(int, input().split())
# visit = [False] * 100001
# print(f(n, k))
