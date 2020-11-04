# 12851
# import heapq
# import sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def bfs(start):
#     q = []
#     heapq.heappush(q, [0, start])
#     ans = [0, INF]
#     while q:
#         sec, place = heapq.heappop(q)
#
#         if place == k:
#             ans[0] += 1
#             ans[1] = sec
#
#         if sec > ans[1]:
#             return ans
#
#         if 0 < sec + 1 <= 100000:
#             heapq.heappush(q, [sec + 1, place + 1])
#             heapq.heappush(q, [sec + 1, place - 1])
#             heapq.heappush(q, [sec + 1, place * 2])
#
#
# n, k = map(int, input().split())
# ans = bfs(n)
# print(ans[1])
# print(ans[0])

from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001

def bfs(start):
    q = deque([[start, 0]])
    ans = 0

    while q:
        place, sec = q.popleft()

        if place == k:
            if not visit[place]:
                visit[place] = sec
                ans += 1
            elif sec == visit[place]:
                ans += 1

        for next in [place+1, place-1, place*2]:
            if 0 <= next < MAX:
                if visit[next] == 0 or visit[next] >= sec+1:
                    if visit[k] and sec+1 > visit[next]:
                        continue

                    visit[next] = sec + 1
                    q.append([next, sec+1])

    print(visit[place])
    print(ans)

n, k = map(int, input().split())
visit = [0 for _ in range(MAX)]
if n >= k:
    print(n-k)
    print(1)
    exit(0)
bfs(n)
