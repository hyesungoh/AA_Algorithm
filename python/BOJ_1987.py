# from collections import deque
# import sys
# input = sys.stdin.readline
# dire = [[0, 1],
#         [0, -1],
#         [1, 0],
#         [-1, 0]]
#
# def return_ord(char):
#     return ord(char) - 65
#
# def check(char, visit, boolean):
#     visit[return_ord(char)] = not visit[return_ord(char)]
#
# def solve():
#     visit = [False for _ in range(26)]
#
#     q = deque()
#     # y, x, cnt
#     q.append([0, 0, 1])
#     check(graph[0][0], visit, True)
#     ans = 0
#
#    while q:
#         y, x, cnt = q.popleft()
#         ans = max(ans, cnt)
#
#         for dy, dx in dire:
#             ny = y + dy
#             nx = x + dx
#             if 0 <= ny < r and 0 <= nx < c:
#                 if not visit[return_ord(graph[ny][nx])]:
#                     check(graph[ny][nx], visit, True)
#                     q.append([ny, nx, cnt+1])
#
#     return ans
#
# r, c = map(int, input().split())
# graph = [input() for _ in range(r)]
# print(solve())


# import sys
# input = sys.stdin.readline
# dire = [[0, 1],
#         [0, -1],
#         [1, 0],
#         [-1, 0]]
#
#
# def solve():
#     q = set([(0, 0, 1, graph[0][0])])
#     ans = 0
#
#     while q:
#         y, x, cnt, visited = q.pop()
#         ans = max(ans, cnt)
#
#         for dy, dx in dire:
#             ny = y + dy
#             nx = x + dx
#             if 0 <= ny < r and 0 <= nx < c:
#                 if graph[ny][nx] not in visited:
#                     q.add((ny, nx, cnt+1, visited + graph[ny][nx]))
#
#     return ans
#
# r, c = map(int, input().split())
# graph = [input() for _ in range(r)]
# print(solve())

import sys
input = sys.stdin.readline

dire = [[0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]]

def bt(y, x, depth):
    global ans
    ans = max(ans, depth)

    for ty, tx in dire:
        ny = y + ty
        nx = x + tx

        if 0 <= ny < r and 0 <= nx < c:
            if not visit[graph[ny][nx]]:
                visit[graph[ny][nx]] = True
                bt(ny, nx, depth+1)
                visit[graph[ny][nx]] = False


r, c = map(int, input().split())
ans = 0
graph = [list(map(lambda x: ord(x) - 65, input())) for _ in range(r)]
visit = [False for _ in range(26)]
visit[graph[0][0]] = True
bt(0, 0, 1)
print(ans)
