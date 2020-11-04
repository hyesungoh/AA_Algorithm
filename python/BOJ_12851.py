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

        if place == k: # 현재 목표 지점일 때
            if not visit[place]: # 첫 방문일 때
                visit[place] = sec # 현재 시간을 저장
                ans += 1 # 카운트 변수에 +1
            elif sec == visit[place]: # 첫방문은 아니지만 시간이 같을 때
                ans += 1 # 카운트 변수에 +1

        for next in [place+1, place-1, place*2]:
            if 0 <= next < MAX: # 범위를 안넘었을 때
                # 다음으로 갈 곳이 첫 방문 혹은 배정될 시간보다 클 때
                if visit[next] == 0 or visit[next] >= sec+1:
                    # 목적지에 저장된 값과 배정될 시간이 다음으로 갈 곳에 저장된 값보다 크면?
                    if visit[k] and sec+1 > visit[next]:
                        # 큐에 추가를 안하여 시간 단축
                        # 목적지의 시간과 다음에 연산될 시긴이 더 크면 연산이 불필요하기 때문
                        continue

                    visit[next] = sec + 1
                    q.append([next, sec+1])

    print(visit[place])
    print(ans)

n, k = map(int, input().split())
visit = [0 for _ in range(MAX)]

if n >= k: # 처음 시작 지점이 목표 지점보다 같거나 클 때
    print(n-k) # 시작 지점 - 목표 지점 (동일 시 0)
    print(1) # -1되는 방법밖에 없음 (동일 시는 아무 연산 안하는 방법 1개)
    exit(0) # 프로그램 종료

bfs(n)
